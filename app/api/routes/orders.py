from fastapi import APIRouter, Body, Query, status
from typing import Annotated
from app.schemas.order import OrderCreateResponse, OrderCreate, OrderListResponse
from app.db.db import get_order_collection
from bson import ObjectId

from bson import ObjectId

router = APIRouter(
  prefix="/orders",
  tags=["orders"]
)



@router.post(
  "/",
  response_model=OrderCreateResponse,
  status_code=status.HTTP_201_CREATED,
  summary="Create a new order",
  description="Adds a new order to the database"
)
async def create_order(order: OrderCreate = Body(...)):
  order_collection = get_order_collection()
  order_dict = order.model_dump()

  for item in order_dict["items"]:
    item["productId"] = ObjectId(item["productId"])

  new_order = await order_collection.insert_one(order_dict)
  return OrderCreateResponse(id=str(new_order.inserted_id))



@router.get(
  "/{user_id}",
  response_model=OrderListResponse,
  status_code=status.HTTP_200_OK,
  summary="Get List of Orders by User",
  description="Retrieves a paginated list of orders for a given user."
)
async def get_orders_by_user(
  user_id: str,
  limit: Annotated[int, Query(description="Number of orders to return", ge=1, le=100)] = 10,
  offset: Annotated[int, Query(description="Number of orders to skip", ge=0)] = 0
):
  order_collection = get_order_collection()

  pipeline = [
    {"$match": {"userId": user_id}},
    {"$sort": {"_id": 1}},
    {"$skip": offset},
    {"$limit": limit},
    {"$unwind": "$items"},
    {
      "$lookup": {
        "from": "products",
        "localField": "items.productId",
        "foreignField": "_id",
        "as": "product_details"
      }
    },
    {"$unwind": "$product_details"},
    {
      "$group": {
        "_id": "$_id",
        "items": {
          "$push": {
            "productDetails": {
              "id": {"$toString": "$product_details._id"},
              "name": "$product_details.name"
            },
            "qty": "$items.qty"
          }
        },
        "total": {"$sum": {"$multiply": ["$items.qty", "$product_details.price"]}}
      }
    },
    {
      "$project": {
        "id": {"$toString": "$_id"},
        "_id": 0,
        "items": 1,
        "total": 1
      }
    }
  ]

  orders_cursor = order_collection.aggregate(pipeline)
  orders = await orders_cursor.to_list(length=limit)

  total_documents = await order_collection.count_documents({"userId": user_id})
  next_offset = offset + limit if offset + limit < total_documents else None
  previous_offset = offset - limit if offset - limit >= 0 else None

  return {
    "data": orders,
    "page": {
      "limit": len(orders),
      "next": next_offset,
      "previous": previous_offset
    }
  }
