import random
import string
from faker import Faker
from pymongo import MongoClient
import time

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["application_db"]

# Create collections
customers_col = db["customers"]
orders_col = db["orders"]
returns_col = db["returns"]

# Create Faker instance
fake = Faker()

# Generate and insert fake data
start_time = time.time()
while time.time() - start_time < 60:
    # Generate customer data
    customer = {"name": fake.name(), "email": fake.email(), "address": fake.address()}
    customer_id = customers_col.insert_one(customer).inserted_id

    # Generate order data
    order = {
        "customer_id": customer_id,
        "product": fake.word(),
        "quantity": random.randint(1, 10),
        "price": random.uniform(10, 100),
    }
    order_id = orders_col.insert_one(order).inserted_id

    # Generate return data
    return_reasons = ["Damaged", "Wrong item", "Not satisfied"]
    return_status = ["Pending", "Approved", "Rejected"]
    return_data = {
        "order_id": order_id,
        "reason": random.choice(return_reasons),
        "status": random.choice(return_status),
    }
    returns_col.insert_one(return_data)

    # Print inserted data for verification
    print(f"Inserted customer: {customer}")
    print(f"Inserted order: {order}")
    print(f"Inserted return: {return_data}")
    print("---")

# Close MongoDB connection
client.close()
