from fastapi import FastAPI
from app.api.routes.products import router as product_router
from app.api.routes.orders import router as order_router

from fastapi import FastAPI
from app.api.routes.products import router as product_router
from app.db.db import connect_to_mongo, close_mongo_connection

app = FastAPI(
  title="E-commerce API",
  description="API for managing products and orders",
  version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
  await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
  await close_mongo_connection()



app.include_router(product_router)
app.include_router(order_router)
