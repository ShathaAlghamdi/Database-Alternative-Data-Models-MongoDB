## Strength, Tradeoffs & Usecases 

### Strength

**1. Flexible Schema**

* With MongoDB you can create documents in one collection that have varying numbers of fields.
* For example, in my POC (Proof of Concept) I created the field "Advanced Python" which has two extra fields ("pages" and "publisher") compared to all of the other books.

**2. Embedded Documents**

* You can embed related data within a single document using MongoDB.
* Author information was embedded into every book in my POC so when I wanted to get both pieces of information at once I didn't have to make another request.

**3. Nested and Array Queries**

* You can query on nested fields and/or arrays with MongoDB.
* To find books written by Sarah I queried on "author.name", and to find books about Python I queried on "tags".

**4. Indexing**

* Indexes enable MongoDB to quickly locate relevant documents without having to scan through the whole collection.
* During my test run there were three documents scanned from the collection; however, only one document was returned after running the indexed query.

### Disadvantages/Tradeoffss

**1. Duplicate Data**

* When you embed author information into multiple books you could potentially end up with duplicate data.
* If an author's name changes then you will likely have to update multiple documents.

**2. Complex Relationships**

* Applications that involve numerous relationships between entities will probably need reference objects and/or additional queries.

**3. Data Consistency**

* While flexible schemas give you flexibility in how you structure your documents, they also introduce the possibility of inconsistent data. Therefore, your application should include validation logic to ensure consistency.

**4. Index Overhead**

* Indexes take up space and require upkeep during write operations.

### Example Uses

**1. E-Commerce Product Catalogs**

* Products can vary greatly based upon their type and therefore may have differing sets of attributes/specifics.

**2. Content Management Systems**

* Pages/articles can be structured differently depending on what kind of content is being published.

**3. User Profiles**

* User profiles can include optional preference/settings.

**4. Library Management**

* Books can include author information, category information, publisher information etc., along with other optional attributes.