 Read all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = list(collection.find())
    users_list = [{'id': str(user['_id']), 'name': user['name'], 'email': user['email']} for user in users]
    return jsonify({'users': users_list})

# Read single user
@app.route('/api/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        return jsonify({'id': str(user['_id']), 'name': user['name'], 'email': user['email']})
    else:
        return jsonify({'message': 'User not found'}), 404

# Update
@app.route('/api/user/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'name': name, 'email': email}})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

# Delete
@app.route('/api/user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)



