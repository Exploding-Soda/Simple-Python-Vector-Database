### 1. **Home Page (`/`)**
   - **Request**:
     - **Method**: `GET`
     - **URL**: `http://localhost:5000/`
   - **Example**:
     ```bash
     curl http://localhost:5000/
     ```

### 2. **Manage Tables (`/tables`)**

   - **Create a New Table (POST)**
     - **Method**: `POST`
     - **URL**: `http://localhost:5000/tables`
     - **Request Body**:
       ```json
       {
         "table_name": "my_table"
       }
       ```
     - **Example**:
       ```bash
       curl -X POST -H "Content-Type: application/json" -d '{"table_name": "my_table"}' http://localhost:5000/tables
       ```

   - **List All Tables (GET)**
     - **Method**: `GET`
     - **URL**: `http://localhost:5000/tables`
     - **Example**:
       ```bash
       curl http://localhost:5000/tables
       ```

### 3. **Delete Table (`/tables/<table_name>`)**
   - **Method**: `DELETE`
   - **URL**: `http://localhost:5000/tables/my_table`
   - **Example**:
     ```bash
     curl -X DELETE http://localhost:5000/tables/my_table
     ```

### 4. **Add Entry to Table (`/tables/<table_name>/entries`)**
   - **Method**: `POST`
   - **URL**: `http://localhost:5000/tables/my_table/entries`
   - **Request Body**:
     ```json
     {
       "text": "This is a sample text to be embedded and stored."
     }
     ```
   - **Example**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a sample text to be embedded and stored."}' http://localhost:5000/tables/my_table/entries
     ```

### 5. **Delete Entry from Table (`/tables/<table_name>/entries/<entry_id>`)**
   - **Method**: `DELETE`
   - **URL**: `http://localhost:5000/tables/my_table/entries/1`
   - **Example**:
     ```bash
     curl -X DELETE http://localhost:5000/tables/my_table/entries/1
     ```

### 6. **List Entries in Table (`/tables/<table_name>/entries`)**
   - **Method**: `GET`
   - **URL**: `http://localhost:5000/tables/my_table/entries`
   - **Example**:
     ```bash
     curl http://localhost:5000/tables/my_table/entries
     ```

### 7. **Query Entries in Table (`/tables/<table_name>/query`)**
   - **Method**: `POST`
   - **URL**: `http://localhost:5000/tables/my_table/query`
   - **Request Body**:
     ```json
     {
       "text": "Find similar entries to this text."
     }
     ```
   - **Example**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "Find similar entries to this text."}' http://localhost:5000/tables/my_table/query
     ```

### 8. **Split Text (`/split_text`)**
   - **Method**: `POST`
   - **URL**: `http://localhost:5000/split_text`
   - **Request Body**:
     ```json
     {
       "text": "This is a long piece of text. It will be split into sentences and chunks!"
     }
     ```
   - **Example**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a long piece of text. It will be split into sentences and chunks!"}' http://localhost:5000/split_text
     ```