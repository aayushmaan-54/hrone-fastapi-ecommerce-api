from pydantic import BaseModel, Field
from typing import List
from app.schemas.common import PageInfo



# Create Product API
class ProductSize(BaseModel):
  size: str
  quantity: int = Field(..., ge=0)


class ProductCreate(BaseModel):
  name: str
  price: float = Field(..., gt=0)
  sizes: List[ProductSize]


class ProductCreateResponse(BaseModel):
  id: str



# List Products API
class ProductPublic(BaseModel):
  id: str
  name: str
  price: float


class ProductListResponse(BaseModel):
  data: List[ProductPublic]
  page: PageInfo
