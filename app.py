from flask import Flask, request, jsonify, render_template
import sqlite3
import requests
import pickle
import numpy as np
import re
from transformers import AutoTokenizer, pipeline

app = Flask(__name__)
DATABASE = 'vector_db.db'
EMBEDDING_API_URL = ''
API_KEY = ''

def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, text TEXT, vector BLOB)')
    conn.commit()
    conn.close()

def delete_table(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    conn.commit()
    conn.close()

def insert_entry(table_name, text, vector):
    conn = create_connection()
    cursor = conn.cursor()
    vector_blob = sqlite3.Binary(pickle.dumps(vector))
    cursor.execute(f'INSERT INTO {table_name} (text, vector) VALUES (?, ?)', (text, vector_blob))
    conn.commit()
    conn.close()

def delete_entry(table_name, entry_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table_name} WHERE id=?', (entry_id,))
    conn.commit()
    conn.close()

def query_entries(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    conn.close()
    deserialized_rows = [{'id': row[0], 'text': row[1]} for row in rows]
    return deserialized_rows

def get_embedding(text):
    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'text-embedding-ada-002',
        'input': text
    }
    response = requests.post(EMBEDDING_API_URL, headers=headers, json=data)
    return response.json()['data'][0]['embedding']

def split_text_into_sentences(text):
    sentences = re.split(r'(?<=[。！？])', text)
    return [s for s in sentences if s]

def split_sentences_to_chunks(sentences, max_chunk_size=200):
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += sentence
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tables', methods=['GET', 'POST'])
def manage_tables():
    if request.method == 'POST':
        table_name = request.json['table_name']
        create_table(table_name)
        return jsonify({'message': f'Table {table_name} created successfully'}), 201
    elif request.method == 'GET':
        tables = list_tables()
        return jsonify(tables), 200

def list_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

@app.route('/tables/<table_name>', methods=['DELETE'])
def delete_existing_table(table_name):
    delete_table(table_name)
    return jsonify({'message': f'Table {table_name} deleted successfully'}), 200

@app.route('/tables/<table_name>/entries', methods=['POST'])
def add_entry_to_table(table_name):
    text = request.json['text']
    vector = get_embedding(text)
    insert_entry(table_name, text, vector)
    return jsonify({'message': 'Entry added successfully'}), 201

@app.route('/tables/<table_name>/entries/<entry_id>', methods=['DELETE'])
def delete_entry_from_table(table_name, entry_id):
    delete_entry(table_name, entry_id)
    return jsonify({'message': 'Entry deleted successfully'}), 200

@app.route('/tables/<table_name>/entries', methods=['GET'])
def list_entries_in_table(table_name):
    entries = query_entries(table_name)
    return jsonify(entries), 200

@app.route('/tables/<table_name>/query', methods=['POST'])
def query_entries_in_table(table_name):
    query_text = request.json['text']
    query_vector = get_embedding(query_text)
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT id, text, vector FROM {table_name}')
    rows = cursor.fetchall()
    conn.close()

    similarities = []

    for row in rows:
        entry_id = row[0]
        text = row[1]
        vector = pickle.loads(row[2])
        similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
        similarities.append({'id': entry_id, 'text': text, 'similarity': similarity})

    similarities = sorted(similarities, key=lambda x: x['similarity'], reverse=True)
    
    top_matches = similarities[:7]

    if top_matches:
        return jsonify(top_matches), 200
    else:
        return jsonify({'message': 'No entries found'}), 404

@app.route('/split_text', methods=['POST'])
def split_text():
    input_text = request.json['text']
    sentences = split_text_into_sentences(input_text)
    chunks = split_sentences_to_chunks(sentences)
    return jsonify(chunks), 200

if __name__ == '__main__':
    app.run(debug=True)
