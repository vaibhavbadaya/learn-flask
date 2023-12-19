from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import bcrypt

app = Flask(__name__)

def mongo_connection():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
    db = client['mydatabase']  # Replace 'mydatabase' with your database name
    collection = db['users']  # Replace 'users' with your collection name

    return collection

def hash_password(raw_password):
    # Hash the raw password using bcrypt
    hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

# Create
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    data["created_at"] = datetime.now()
    raw_password = data.get("password")

    hashed_password = hash_password(raw_password)
    data["password"] = hashed_password
    collection = mongo_connection()
    result = collection.insert_one(data)
    return jsonify({'message': 'User created successfully', 'id': str(result.inserted_id)})

@app.route('/api/sayhello', methods=['GET'])
def say_hello():
    return jsonify({' message': "Hello India Welcome to new year 2024"})

if __name__ == '__main__':
    # Run Flask on a specific host and port
    app.run(host='0.0.0.0', port=8000)

