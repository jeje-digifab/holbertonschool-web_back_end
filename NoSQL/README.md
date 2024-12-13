### Tasks Summary for README

This project involves a series of tasks related to MongoDB and Python scripting for database operations. Below is a summary of each task:

1. **List all databases**
   - **Script**: `0-list_databases`
   - **Description**: Lists all databases in MongoDB.
   - **Usage**: `cat 0-list_databases | mongo`

2. **Create a database**
   - **Script**: `1-use_or_create_database`
   - **Description**: Creates or uses the database `my_db`.
   - **Usage**: `cat 1-use_or_create_database | mongo`

3. **Insert document**
   - **Script**: `2-insert`
   - **Description**: Inserts a document with the attribute `name` set to "Holberton school" into the `school` collection.
   - **Usage**: `cat 2-insert | mongo my_db`

4. **All documents**
   - **Script**: `3-all`
   - **Description**: Lists all documents in the `school` collection.
   - **Usage**: `cat 3-all | mongo my_db`

5. **All matches**
   - **Script**: `4-match`
   - **Description**: Lists all documents with `name="Holberton school"` in the `school` collection.
   - **Usage**: `cat 4-match | mongo my_db`

6. **Count**
   - **Script**: `5-count`
   - **Description**: Displays the number of documents in the `school` collection.
   - **Usage**: `cat 5-count | mongo my_db`

7. **Update**
   - **Script**: `6-update`
   - **Description**: Adds the attribute `address` with the value "972 Mission street" to documents with `name="Holberton school"`.
   - **Usage**: `cat 6-update | mongo my_db`

8. **Delete by match**
   - **Script**: `7-delete`
   - **Description**: Deletes all documents with `name="Holberton school"` in the `school` collection.
   - **Usage**: `cat 7-delete | mongo my_db`

9. **List all documents in Python**
   - **Script**: `8-all.py`
   - **Description**: Python function to list all documents in a collection.
   - **Usage**: `./8-main.py`

10. **Insert a document in Python**
    - **Script**: `9-insert_school.py`
    - **Description**: Python function to insert a new document in a collection based on keyword arguments.
    - **Usage**: `./9-main.py`

11. **Change school topics**
    - **Script**: `10-update_topics.py`
    - **Description**: Python function to change all topics of a school document based on the name.
    - **Usage**: `./10-main.py`

12. **Where can I learn Python?**
    - **Script**: `11-schools_by_topic.py`
    - **Description**: Python function to return the list of schools having a specific topic.
    - **Usage**: `./11-main.py`

13. **Log stats**
    - **Script**: `12-log_stats.py`
    - **Description**: Python script to provide stats about Nginx logs stored in MongoDB.
    - **Usage**: `./12-log_stats.py`

### Repository Details
- **GitHub Repository**: `holbertonschool-web_back_end`
- **Directory**: `NoSQL`

Each script and function is designed to interact with a MongoDB database, performing various operations such as listing, inserting, updating, and deleting documents, as well as providing statistical information.
