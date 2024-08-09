
# A simple Embedding Vector Database

## Overview

This project provides a RESTful API service for managing text data and its corresponding embedding vectors. The service allows you to create tables, store text data along with their embedding vectors, and query the most similar texts from the stored entries. It also includes features for splitting text into sentences and manageable chunks.

This project is particularly useful in scenarios involving Natural Language Processing (NLP), where you might need to store, retrieve, and compare textual data based on their semantic meaning.

## Features

- **Table Management**: Create, list, and delete tables in the SQLite database.
- **Text Data Management**: Insert, delete, and list text entries in tables along with their embedding vectors.
- **Similarity Query**: Query the most similar entries based on a given text input.
- **Text Processing**: Split a long text into sentences and further into manageable chunks.

## Prerequisites

- Python 3.x
- `pip` for installing Python dependencies
- SQLite for database management

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Exploding-Soda/Simple-Python-Vector-Database
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   - `EMBEDDING_API_URL`: The URL for the embedding generation API.
   - `API_KEY`: Your API key for accessing the embedding generation service.

   Example:
   ```bash
   export EMBEDDING_API_URL='https://api.example.com/embedding'
   export API_KEY='your-api-key'
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

   The application will start on `http://localhost:5000`.

## API Endpoints

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

## Usage

1. **Create a Table**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"table_name": "my_table"}' http://localhost:5000/tables
   ```

2. **Add an Entry**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "Sample text to store"}' http://localhost:5000/tables/my_table/entries
   ```

3. **Query for Similar Entries**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "Query text to find similar"}' http://localhost:5000/tables/my_table/query
   ```

4. **List All Entries**:
   ```bash
   curl http://localhost:5000/tables/my_table/entries
   ```

5. **Delete a Table**:
   ```bash
   curl -X DELETE http://localhost:5000/tables/my_table
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
