from fastapi import APIRouter, Body, Query, status
from typing import Annotated
from app.schemas.product import ProductCreateResponse, ProductCreate, ProductListResponse
from app.db.db import get_product_collection


router = APIRouter(
  prefix="/products",
  tags=["products"]
)



@router.post(
  "/",
  response_model=ProductCreateResponse,
  status_code=status.HTTP_201_CREATED,
  summary="Create a new product",
  description="Adds a new product to the database"
)
async def create_product(product: ProductCreate = Body(...)):
  product_collection = get_product_collection()
  product_dict = product.model_dump()
  new_product = await product_collection.insert_one(product_dict)
  return ProductCreateResponse(id=str(new_product.inserted_id))



@router.get(
  "/",
  response_model=ProductListResponse,
  status_code=status.HTTP_200_OK,
  summary="List Products API",
  description="Retrieves a paginated list of products with optional filters."
)
async def get_products(
  name: Annotated[str | None, Query(description="Product name to search (partial)")] = None,
  size: Annotated[str | None, Query(description="Product size filter")] = None,
  limit: Annotated[int, Query(description="Number of products to return", ge=1, le=100)] = 10,
  offset: Annotated[int, Query(description="Number of products to skip", ge=0)] = 0
):
  product_collection = get_product_collection()
  query = {}

  if name:
    query["name"] = {"$regex": name, "$options": "i"}

  if size:
    query["sizes"] = {"$elemMatch": {"size": size}}

  products_cursor = product_collection.find(query).sort("_id", 1).skip(offset).limit(limit)
  products = await products_cursor.to_list(length=limit)
  total_documents = await product_collection.count_documents(query)

  next_offset = offset + limit if offset + limit < total_documents else None
  previous_offset = offset - limit if offset - limit >= 0 else None

  return {
    "data": [
      {"id": str(p["_id"]), "name": p["name"], "price": p["price"]}
        for p in products
      ],
    "page": {
      "limit": len(products),
      "next": next_offset,
      "previous": previous_offset
    }
  }
