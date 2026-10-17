# Research Summary: Document Data Model – MongoDB

**Project:** Database Alternative Data Models  
**Database Model:** Document  
**Database System:** MongoDB 8.0

## 1. Introduction

A Document Database is a type of NoSQL database that stores data as documents rather than rows and columns.

MongoDB is a document-oriented database that stores records in BSON (Binary JSON), a format similar to JSON that supports additional types of data.

Document databases are useful for applications that require flexible data structures, nested information, and changing data requirements.

## 2. How MongoDB Organizes Data

MongoDB organizes data into three main levels:

- **Database:** Contains collections.
- **Collection:** Contains related documents.
- **Document:** Contains fields and values.

In our project, we created a database called `library_db` and a collection called `books`.

Example:

```json
{
  "title": "Python Basics",
  "author": {
    "name": "Sarah",
    "country": "Saudi Arabia"
  },
  "price": 80,
  "tags": ["Python", "Programming"],
  "available": true
}
```

The `author` field is an embedded document, while `tags` is an array.

MongoDB assigns a unique `_id` to each document if one is not provided.

## 3. Core Concepts

### Flexible Schema

MongoDB allows documents in the same collection to have different fields.

In our POC, the book `Advanced Python` contains additional fields such as `pages` and `publisher`, while other books do not.

### Embedded Documents and Arrays

Documents can contain nested objects and arrays, allowing related data to be stored together.

### Embedding vs Referencing

Embedding stores related information within the same document.

Referencing stores an identifier pointing to another document, often in a different collection.

The appropriate choice depends on how the application reads and updates related data.

### Indexing

Indexes help MongoDB locate matching documents efficiently.

Indexes also require additional storage and maintenance during write operations.

## 4. Basic Database Operations (CRUD)

MongoDB supports four basic operations:

| Operation | PyMongo Method | Purpose |
|---|---|---|
| Create | `insert_one()` | Add a document |
| Read | `find()` / `find_one()` | Retrieve documents |
| Update | `update_one()` | Modify a document |
| Delete | `delete_one()` | Remove a document |

In our application, we also used:

- `upsert=True` to insert sample data when no matching document exists.
- `$setOnInsert` to provide fields only when a new document is inserted.
- `$set` to update the nested field `publisher.city`.
- Dot notation such as `author.name` to query embedded information.

## 5. Strengths

1. **Flexible data structure:** Documents can have different fields.
2. **Nested data support:** Related information can be stored together.
3. **Expressive queries:** Queries can target nested fields and arrays.
4. **Indexing:** Indexes can reduce the number of documents examined.
5. **Scalability:** MongoDB supports horizontal scaling through sharding.

## 6. Limitations and Trade-offs

1. Embedding shared information in multiple documents may lead to duplication.
2. Complex relationships require careful decisions about embedding and referencing.
3. Flexible schemas may require validation to ensure consistency.
4. Indexes consume storage and introduce maintenance overhead.
5. Database performance depends on document design, query patterns, and indexing.

## 7. Common Use Cases

- **E-commerce:** Product catalogs with various attributes.
- **Content Management:** Articles and pages with flexible content.
- **User Profiles:** Optional preferences and settings.
- **Library Systems:** Books, authors, categories, and publisher details.

## 8. Practical Findings from Our POC

Our application utilized MongoDB 8.0 running inside Docker, with Python and PyMongo as the client.

We successfully demonstrated:

- Connecting Python to MongoDB.
- Inserting and retrieving book documents.
- Different document structures in one collection.
- Querying nested fields and arrays.
- Updating a nested field.
- Deleting a temporary document.
- Comparing collection scanning and indexed querying.

### Indexing Experiment

| Query Approach | Documents Examined |
|---|---:|
| Forced collection scan | 3 |
| Forced title index scan | 1 |

The indexed query examined fewer documents in our small dataset. However, this does not indicate an equivalent improvement in execution speed.

## 9. Conclusion

MongoDB offers a flexible approach to storing and managing document-oriented data.

Through our library POC, we gained knowledge on structuring documents, executing CRUD operations, querying nested fields, and experimenting with indexing.

MongoDB is beneficial when document flexibility and embedded data align with the requirements of the application. Relational databases may be preferred when strong relationships, constraints, and structured transactions are central to the application.

## References

1. MongoDB Documentation — Documents  
   https://www.mongodb.com/docs/manual/core/document/

2. MongoDB Documentation — Data Modeling  
   https://www.mongodb.com/docs/manual/data-modeling/

3. MongoDB Documentation — CRUD Operations  
   https://www.mongodb.com/docs/manual/crud/

4. MongoDB Documentation — Indexes  
   https://www.mongodb.com/docs/manual/indexes/

5. MongoDB Documentation — Document Relationships  
   https://www.mongodb.com/docs/manual/applications/data-models-relationships/

6. MongoDB PyMongo Driver Documentation  
   https://www.mongodb.com/docs/languages/python/pymongo-driver/current/