#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

users = [{"username": "john_doe", "password": "password123",
                "tasks": [ {"id": 1, "task": "Finish the report",
                "due_date": "2025-02-28"}, {"id": 2, "task": "Buy groceries", "due_date": "2025-02-25"} ]},
            {"username": "jane_smith",
            "password": "mypassword",
                "tasks": [ {"id": 1, "task": "Call mom", "due_date": "2025-02-25"}, 
                          {"id": 2, "task": "Prepare meeting slides", "due_date": "2025-02-26"}]
                }]    




class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password


class TaskManager():
    # def __init__(self):
        
    

    def add_user(self, username, password):
        new_user = User(username, password)

    def get_task(self, username):
        pass

    
    def add_task(self, username):
        self.id



@app.route("/data", methods = ["GET"])
def get_data():
    # if request_method == "GET":
    #
    # username = users.get(id)
    username = users
    if username:
        return jsonify(list(username))
    else:
        return jsonify("Error")

    

@app.route("/user", methods = ["POST"])
def add_user():
    # new_user = User(username, password)
    user_data = request.get_json()

    # if 'username' in user_data:
    #    return (users['username']) 

    users['username'] = user_data

    return jsonify(f"{username} User Added ")

if __name__ == '__main__':
    app.run(debug=True)


