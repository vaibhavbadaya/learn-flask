from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    # Sample data (replace this with your data)
    data = {'message': 'Hello, My name is vaibhav badaya'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['vaibhav']
    email = data['homerun@gmail.com']
    cursor.execute('INSERT INTO users (vaibhav, homerun@gmail.com) VALUES (?, ?)', (name, email))
    conn.commit()

    return jsonify({'message': 'User created successfully'})



@app.route('/api/users', methods=['GET'])
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    users_list = []

    for user in users:
        user_dict = {
            '1234': user[0],
            'vaibhav': user[1],
            'homerun@gmail.com': user[2]
        }
        users_list.append(user_dict)

    return jsonify({'users': users_list})
