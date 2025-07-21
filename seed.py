import asyncio
import random
from app.db.db import connect_to_mongo, close_mongo_connection, get_database



async def seed_products():
  print("🌱 Starting database seeding...")

  db = get_database()
  if db is None:
    print("❌ Database connection not found. Aborting.")
    return

  product_collection = db["products"]

  await product_collection.delete_many({})
  print("🗑️  Cleared existing products collection.")

  products_data = [
    {"name":"Classic White T-Shirt","price":299.0,"sizes":[{"size":"S","quantity":50},{"size":"M","quantity":40},{"size":"L","quantity":30}]},
    {"name":"Blue Denim Jeans","price":999.0,"sizes":[{"size":"30","quantity":20},{"size":"32","quantity":25},{"size":"34","quantity":15}]},
    {"name":"Black Hoodie","price":799.0,"sizes":[{"size":"M","quantity":35},{"size":"L","quantity":20},{"size":"XL","quantity":10}]},
    {"name":"Red Sports Cap","price":199.0,"sizes":[{"size":"Free","quantity":100}]},
    {"name":"Leather Wallet","price":499.0,"sizes":[{"size":"Standard","quantity":70}]},
    {"name":"Running Shoes","price":1299.0,"sizes":[{"size":"7","quantity":20},{"size":"8","quantity":25},{"size":"9","quantity":15}]},
    {"name":"Black Formal Shoes","price":1499.0,"sizes":[{"size":"8","quantity":10},{"size":"9","quantity":15},{"size":"10","quantity":10}]},
    {"name":"Cotton Socks Pack","price":149.0,"sizes":[{"size":"Free","quantity":200}]},
    {"name":"Brown Leather Belt","price":299.0,"sizes":[{"size":"M","quantity":40},{"size":"L","quantity":30}]},
    {"name":"Checked Shirt","price":699.0,"sizes":[{"size":"S","quantity":20},{"size":"M","quantity":30},{"size":"L","quantity":25}]},
    {"name":"Striped Polo T-Shirt","price":499.0,"sizes":[{"size":"S","quantity":30},{"size":"M","quantity":35},{"size":"L","quantity":20}]},
    {"name":"Winter Jacket","price":1999.0,"sizes":[{"size":"M","quantity":10},{"size":"L","quantity":8},{"size":"XL","quantity":5}]},
    {"name":"Casual Shorts","price":399.0,"sizes":[{"size":"S","quantity":20},{"size":"M","quantity":15},{"size":"L","quantity":10}]},
    {"name":"Black Track Pants","price":599.0,"sizes":[{"size":"M","quantity":25},{"size":"L","quantity":20},{"size":"XL","quantity":10}]},
    {"name":"Cotton Handkerchief","price":99.0,"sizes":[{"size":"Free","quantity":150}]},
    {"name":"Printed Kurta","price":799.0,"sizes":[{"size":"M","quantity":20},{"size":"L","quantity":15},{"size":"XL","quantity":10}]},
    {"name":"Silk Tie","price":249.0,"sizes":[{"size":"Standard","quantity":50}]},
    {"name":"Wrist Watch","price":1999.0,"sizes":[{"size":"Free","quantity":30}]},
    {"name":"Sunglasses","price":899.0,"sizes":[{"size":"Standard","quantity":40}]},
    {"name":"Black Backpack","price":1299.0,"sizes":[{"size":"Standard","quantity":20}]},
    {"name":"Laptop Sleeve","price":499.0,"sizes":[{"size":"13 inch","quantity":15},{"size":"15 inch","quantity":10}]},
    {"name":"Gym Bag","price":699.0,"sizes":[{"size":"Standard","quantity":25}]},
    {"name":"Earbuds","price":1499.0,"sizes":[{"size":"Standard","quantity":30}]},
    {"name":"Travel Mug","price":299.0,"sizes":[{"size":"350ml","quantity":40}]},
    {"name":"Yoga Mat","price":599.0,"sizes":[{"size":"Standard","quantity":30}]},
    {"name":"Fitness Band","price":1799.0,"sizes":[{"size":"Standard","quantity":20}]},
    {"name":"Bluetooth Speaker","price":1299.0,"sizes":[{"size":"Standard","quantity":25}]},
    {"name":"Graphic T-Shirt","price":399.0,"sizes":[{"size":"S","quantity":20},{"size":"M","quantity":20},{"size":"L","quantity":15}]},
    {"name":"Printed Mug","price":199.0,"sizes":[{"size":"Standard","quantity":50}]},
    {"name":"Ceramic Plate Set","price":799.0,"sizes":[{"size":"6 pieces","quantity":20}]},
    {"name":"Kitchen Apron","price":249.0,"sizes":[{"size":"Standard","quantity":30}]},
    {"name":"Chef Hat","price":199.0,"sizes":[{"size":"Standard","quantity":20}]},
    {"name":"Bath Towel","price":349.0,"sizes":[{"size":"Standard","quantity":40}]},
    {"name":"Hand Towel","price":149.0,"sizes":[{"size":"Standard","quantity":60}]},
    {"name":"Bathroom Slippers","price":199.0,"sizes":[{"size":"M","quantity":20},{"size":"L","quantity":20}]},
    {"name":"Cotton Bedsheet","price":799.0,"sizes":[{"size":"Queen","quantity":10},{"size":"King","quantity":10}]},
    {"name":"Pillow Cover Set","price":299.0,"sizes":[{"size":"2 pieces","quantity":50}]},
    {"name":"Table Lamp","price":499.0,"sizes":[{"size":"Standard","quantity":15}]},
    {"name":"Desk Organizer","price":349.0,"sizes":[{"size":"Standard","quantity":30}]},
    {"name":"Pen Set","price":149.0,"sizes":[{"size":"3 pieces","quantity":100}]},
    {"name":"Notebook","price":99.0,"sizes":[{"size":"A5","quantity":70}]},
    {"name":"Wall Clock","price":599.0,"sizes":[{"size":"Standard","quantity":20}]},
    {"name":"Photo Frame","price":249.0,"sizes":[{"size":"5x7","quantity":40}]},
    {"name":"Portable Charger","price":899.0,"sizes":[{"size":"10,000mAh","quantity":25}]},
    {"name":"USB Cable","price":99.0,"sizes":[{"size":"1m","quantity":100}]},
    {"name":"Extension Board","price":399.0,"sizes":[{"size":"4 sockets","quantity":20}]},
    {"name":"LED Bulb Pack","price":299.0,"sizes":[{"size":"2 pieces","quantity":50}]},
    {"name":"Smart Plug","price":699.0,"sizes":[{"size":"Standard","quantity":15}]},
    {"name":"Wireless Mouse","price":499.0,"sizes":[{"size":"Standard","quantity":30}]},
    {"name":"Keyboard","price":799.0,"sizes":[{"size":"Standard","quantity":20}]},
  ]

  result = await product_collection.insert_many(products_data)
  print(f"✅ Inserted {len(result.inserted_ids)} products.")



async def seed_orders():
  print("🌱 Starting order seeding...")
  db = get_database()
  if db is None:
      print("❌ Database connection not found. Aborting.")
      return

  order_collection = db["orders"]
  product_collection = db["products"]

  await order_collection.delete_many({})
  print("🗑️  Cleared existing orders collection.")

  product_ids = await product_collection.find({}, {"_id": 1}).to_list(length=None)
  product_ids = [p["_id"] for p in product_ids]

  orders_data = []
  for _ in range(50):
    order_items = []
    for _ in range(random.randint(1, 5)):
      order_items.append({
        "productId": random.choice(product_ids),
        "qty": random.randint(1, 10)
      })

      orders_data.append({
        "userId": f"user{random.randint(1, 10)}",
        "items": order_items
      })

  result = await order_collection.insert_many(orders_data)
  print(f"✅ Inserted {len(result.inserted_ids)} orders.")



async def main():
  await connect_to_mongo()
  await seed_products()
  await seed_orders()
  await close_mongo_connection()
  print("🎉 Database seeding completed successfully!")



if __name__ == "__main__":
  asyncio.run(main())
