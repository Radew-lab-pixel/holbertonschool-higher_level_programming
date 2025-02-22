#!/usr/bin/python3

from flask import Flask
from flask import jsonify
app = Flask(__name__)

"""
users = {
    "jane": {"name": "Jane",
             "age": 28,
             "city": "Los Angeles"
             }}
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
    # return jsonify({list(users.keys())})
    return jsonify(users)

""" data function specific to a user jane for debugging """
@app.route("/jane_test")
def jane():
    # return jsonify(users.keys == "jane")  # wrong 
    return jsonify(users['jane'])


""" data function specific to a particular user """
@app.route("/users/<string:id>")  # flask a bit like html format
def user(id):
    return jsonify(users[id])

""" function to return status """
@app.route("/status")
def status():
    return ("OK")

if __name__ == '__main__':
    app.run(debug=True)

