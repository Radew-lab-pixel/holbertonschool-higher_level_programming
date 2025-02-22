#!/usr/bin/python3

from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False

"""
users = {
    "jane": {"name": "Jane",
             "age": 28,
             "city": "Los Angeles"
             }}
"""
"""
users = {
    "jane": {"username": "jane",
              "name": "Jane",
              "age": 28,
              "city": "Los Angeles"
              },
    "john": {"username": "john",
             "name": "John",
             "age": 30,
             "city": "New York"
             }}
"""
users = {}


""" home function"""
@app.route('/')
@app.route('/home')
def home():
    return "Welcome to the Flask API!"
    # pass

""" data function"""
@app.route("/data")
def data():
    # return jsonify(users, status=200, mimetype='application/json')
    # return jsonify({'users': users})
    # return jsonify(users), 200
    # return jsonify({"users": list(users.keys())})
    # return "Testing"
    return jsonify(list(users.keys()))  # has to be implemented to pass checker
    #return jsonify(users)  # work in local terminal but failed checker

""" data function specific to a user jane for debugging """
@app.route("/jane_test")
def jane():
    # return jsonify(users.keys == "jane")  # wrong 
    return jsonify(users['jane'])


""" data function specific to a particular user """
@app.route("/users/<string:id>")  # flask a bit like html format
def user(id):
    username = users.get(id)
    if username is None:
        return {"error": "User not found"}, 404
    else:
        # return jsonify(users[id]), 201
        # data_user = {"username": id, "name": username["name"], "age": username["age"], "city": username["city"]}
        # data_user = {"city": username["city"], "age": username["age"], "name": username["name"], "username": id}    
        # return jsonify(data_user), 201  # failed checker but worked in local terminal
        return jsonify(username)
        # return jsonify(users[id])
        # return jsonify(f"username: {id} {username}")
        # return jsonify(users[id])

""" function to return status """
@app.route("/status")
def status():
    return ("OK")

""" function to add a user """
"""
@app.route('/add_user', methods=['POST'])
def add_user():


    def add_user():
        user_data = request.get_json()  # convert to json string
        # username = user_data['username']
    username = user_data("username")
    if username is None:
        return {"error": "User not found"}, 404
    
    users[username] = user_data
    return { "message": "User added successfully",
            "user": user_data}, 201
"""
@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()  # Parse JSON data from request
    
    # Check if 'username' exists in the received data
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    # print(username)
    # users[username] = user_data
    users[username] = {"username":user_data["username"], "name": user_data["name"], "age": user_data["age"], "city": user_data["city"]}
    return jsonify({
        "message": "User added", "user": user_data}), 200
        #"message": "User added", "user": users[username]}), 201

if __name__ == '__main__':
    app.run(debug=True)

