
# 一个简单的向量数据库

## 概述

该项目提供了一个 RESTful API 服务，用于管理文本数据及其对应的嵌入向量。该服务允许您创建表格，存储文本数据及其嵌入向量，并根据查询文本检索最相似的已存文本。它还包括将文本分割成句子和可管理的块的功能。

该项目在涉及自然语言处理（NLP）的场景中特别有用，例如您可能需要存储、检索和基于语义比较文本数据的场景。

## 功能

- **表格管理**: 创建、列出和删除 SQLite 数据库中的表格。
- **文本数据管理**: 在表格中插入、删除和列出文本条目及其嵌入向量。
- **相似性查询**: 基于给定的文本输入查询最相似的条目。
- **文本处理**: 将长文本分割成句子并进一步分割成可管理的块。

## 先决条件

- Python 3.x
- 用于安装 Python 依赖项的 `pip`
- 用于数据库管理的 SQLite

## 安装步骤

1. **克隆仓库**:
   ```bash
   git clone https://github.com/Exploding-Soda/Simple-Python-Vector-Database.git
   ```

2. **安装依赖项**:
   ```bash
   pip install -r requirements.txt
   ```

3. **设置环境变量**:
   - `EMBEDDING_API_URL`: 嵌入生成 API 的 URL。
   - `API_KEY`: 访问嵌入生成服务的 API 密钥。

   示例:
   ```bash
   export EMBEDDING_API_URL='https://api.example.com/embedding'
   export API_KEY='your-api-key'
   ```

4. **运行应用程序**:
   ```bash
   python app.py
   ```

   应用程序将启动在 `http://localhost:5000`。

## API 端点

### 1. **主页 (`/`)**
   - **请求**:
     - **方法**: `GET`
     - **URL**: `http://localhost:5000/`
   - **示例**:
     ```bash
     curl http://localhost:5000/
     ```

### 2. **管理表格 (`/tables`)**

   - **创建新表格 (POST)**
     - **方法**: `POST`
     - **URL**: `http://localhost:5000/tables`
     - **请求体**:
       ```json
       {
         "table_name": "my_table"
       }
       ```
     - **示例**:
       ```bash
       curl -X POST -H "Content-Type: application/json" -d '{"table_name": "my_table"}' http://localhost:5000/tables
       ```

   - **列出所有表格 (GET)**
     - **方法**: `GET`
     - **URL**: `http://localhost:5000/tables`
     - **示例**:
       ```bash
       curl http://localhost:5000/tables
       ```

### 3. **删除表格 (`/tables/<table_name>`)**
   - **方法**: `DELETE`
   - **URL**: `http://localhost:5000/tables/my_table`
   - **示例**:
     ```bash
     curl -X DELETE http://localhost:5000/tables/my_table
     ```

### 4. **向表格添加条目 (`/tables/<table_name>/entries`)**
   - **方法**: `POST`
   - **URL**: `http://localhost:5000/tables/my_table/entries`
   - **请求体**:
     ```json
     {
       "text": "这是一段要嵌入并存储的示例文本。"
     }
     ```
   - **示例**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "这是一段要嵌入并存储的示例文本。"}' http://localhost:5000/tables/my_table/entries
     ```

### 5. **删除表格中的条目 (`/tables/<table_name>/entries/<entry_id>`)**
   - **方法**: `DELETE`
   - **URL**: `http://localhost:5000/tables/my_table/entries/1`
   - **示例**:
     ```bash
     curl -X DELETE http://localhost:5000/tables/my_table/entries/1
     ```

### 6. **列出表格中的条目 (`/tables/<table_name>/entries`)**
   - **方法**: `GET`
   - **URL**: `http://localhost:5000/tables/my_table/entries`
   - **示例**:
     ```bash
     curl http://localhost:5000/tables/my_table/entries
     ```

### 7. **查询表格中的条目 (`/tables/<table_name>/query`)**
   - **方法**: `POST`
   - **URL**: `http://localhost:5000/tables/my_table/query`
   - **请求体**:
     ```json
     {
       "text": "查找与此文本相似的条目。"
     }
     ```
   - **示例**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "查找与此文本相似的条目。"}' http://localhost:5000/tables/my_table/query
     ```

### 8. **拆分文本 (`/split_text`)**
   - **方法**: `POST`
   - **URL**: `http://localhost:5000/split_text`
   - **请求体**:
     ```json
     {
       "text": "这是一段较长的文本。它将被拆分成句子和块！"
     }
     ```
   - **示例**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "这是一段较长的文本。它将被拆分成句子和块！"}' http://localhost:5000/split_text
     ```

## 使用

1. **创建表格**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"table_name": "my_table"}' http://localhost:5000/tables
   ```

2. **添加条目**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "存储的示例文本"}' http://localhost:5000/tables/my_table/entries
   ```

3. **查询相似条目**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "查找相似的查询文本"}' http://localhost:5000/tables/my_table/query
   ```

4. **列出所有条目**:
   ```bash
   curl http://localhost:5000/tables/my_table/entries
   ```

5. **删除表格**:
   ```bash
   curl -X DELETE http://localhost:5000/tables/my_table
   ```

## 许可

该项目根据 MIT 许可证授权 - 详情请参阅 [LICENSE](LICENSE) 文件。
