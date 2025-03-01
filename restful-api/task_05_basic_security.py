#!/usr/bin/python3
from flask import Flask, request
from flask import jsonify
import jwt

''' source code from https://flask-httpauth.readthedocs.io/en/latest/ '''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

''' have error
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False
'''
''' have error 
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    else:
        return False
'''    
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)  # get value which nested dict of username
    if user and check_password_hash(user['password'], password):
        # return username
        return user
    else:
        return False
    
''' basic protection'''
@app.route('/basic-protection')
@auth.login_required
def basic_protection():
    return "Basic Auth: Access Granted"

''' root '''
@app.route('/')
# @app.route('/basic-protection')
@auth.login_required
def index():
    # return f"Hello {auth.current_user()}"
    return f"Hello {(auth.current_user())['username']}"

''' source code from https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/'''

# route for logging user in
@app.route('/login', methods =['POST'])
def login():
    input = request.get_json()  # convert input to json string as stored as input attr
    username = input['username']
    password = input['password']
    if username is None:
        return {"message": "Missing user name"}, 401
    if password is None:
        return {"message": "Missing password"}, 401
    
    # Check if user exists and password is correct
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Create JWT token with user identity (username + role)
        access_token = create_access_token(identity={
            'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401
 

if __name__ == '__main__':
    app.run(debug=True)
# plain_text_password = "My random password"
# hashed_password = generate_password_hash(plain_text_password) # hashed password
#print("Hashed password ==>", hashed_password)
# check if hashed password matches the plain text password
# print("Checking password ==>", check_password_hash(hashed_password, plain_text_password))