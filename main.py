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

    books.update_one(
    {"title": book["title"]},
    {"$setOnInsert": book},
    upsert=True
    )

    print("Book is ready!")

   
    # Demonstrate flexible schema
    additional_books = [
        {
            "title": "Learn SQL",
            "author": {
                "name": "Ahmed",
                "country": "Saudi Arabia"
            },
            "price": 95,
            "tags": ["SQL", "Database"],
            "available": True
        },
        {
            "title": "Advanced Python",
            "author": {
                "name": "Sarah",
                "country": "Saudi Arabia"
            },
            "price": 150,
            "tags": ["Python", "Advanced"],
            "available": False,
            "pages": 450,
            "publisher": {
                "name": "Tech Press",
                "city": "Riyadh"
            }
        }
    ]

    for book_data in additional_books:
        books.update_one(
            {"title": book_data["title"]},
            {"$setOnInsert": book_data},
            upsert=True
        )

    print("Flexible schema documents are ready!")

    # ----------------------- #
    # Query nested documents
    print("\nBooks written by Sarah:")

    for item in books.find({"author.name": "Sarah"}):
        print(item["title"])

    # Query arrays
    print("\nBooks with Python tag:")

    for item in books.find({"tags": "Python"}):
        print(item["title"])

    # Query by price
    print("\nBooks with price greater than 100:")

    for item in books.find({"price": {"$gt": 100}}):
        print(item["title"])





except ConnectionFailure as error:
    print("MongoDB connection failed:", error)

finally:
    client.close()