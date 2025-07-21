from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes.products import router as product_router
from app.api.routes.orders import router as order_router
from app.db.db import connect_to_mongo, close_mongo_connection



@asynccontextmanager
async def lifespan(app: FastAPI):
  await connect_to_mongo()
  yield
  await close_mongo_connection()


app = FastAPI(
  title="E-commerce API",
  description="API for managing products and orders",
  version="1.0.0",
  lifespan=lifespan
)


app.include_router(product_router)
app.include_router(order_router)
