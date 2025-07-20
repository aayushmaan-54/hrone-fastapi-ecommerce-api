from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.common import PageInfo

# Create Order API
class OrderItemCreate(BaseModel):
    productId: str
    qty: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItemCreate]

class OrderCreateResponse(BaseModel):
    id: str

# Get List of Orders by User
class ProductDetails(BaseModel):
    id: str
    name: str

class OrderItemPublic(BaseModel):
    productDetails: ProductDetails
    qty: int

class OrderPublic(BaseModel):
    id: str
    items: List[OrderItemPublic]
    total: float

class OrderListResponse(BaseModel):
    data: List[OrderPublic]
    page: PageInfo