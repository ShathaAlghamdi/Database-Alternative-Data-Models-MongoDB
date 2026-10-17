from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Connect to MongoDB running in Docker
client = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=5000
)

try:
    # Check MongoDB connection
    client.admin.command("ping")
    print("Connected to MongoDB successfully!")

    # Select database and collection
    db = client["library_db"]
    books = db["books"]

    # Insert our first document
    book = {
        "title": "Python Basics",
        "author": {
            "name": "Sarah",
            "country": "Saudi Arabia"
        },
        "price": 80,
        "tags": ["Python", "Programming"],
        "available": True
    }

    result = books.insert_one(book)
    print("Book inserted:", result.inserted_id)

    # Read documents
    print("\nBooks in database:")
    for item in books.find():
        print(item)

except ConnectionFailure as error:
    print("MongoDB connection failed:", error)

finally:
    client.close()