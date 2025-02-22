### Week 18 : RESTful API

## Task 2 : At the end of this exercise, students should be able to:

    Utilize the requests library to send HTTP requests and process responses.
    Parse and manipulate JSON data using Python.
    Convert structured data into other formats, e.g., CSV.

task_02_requests.py

#!/usr/bin/python3
"""Consuming and processing data from an API using Python 
"""
import requests
import csv
import json


file_name = "posts.csv"

def fetch_and_print_posts():
    """method to fetch and print posts from jsonplaceholder""" 
    # response = requests.get("https://jsonplaceholder.typicode.com/posts/1") # for debugging
    # response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # count = 0  # counter for no, of posts 
    count = 1  # API valid ID (1- 100)
    url = f"https://jsonplaceholder.typicode.com/posts/{count}"
    
    response = requests.get(url, timeout=3)
    # response = requests.head(url)
    # print(response)
    print(f"Status Code: {response.status_code}")

    while response:
        if response:
            # print(response)  # for debugging
            # print(response.json())
            API_data = response.json()
            # print(API_data)
            print(API_data['title'])      
        else:
            raise Exception(f"{response.status_code}")
        count += 1
        url = f"https://jsonplaceholder.typicode.com/posts/{count}"
        response = requests.get(url, timeout=3)

def fetch_and_save_posts():
    """ method to fetch and save posts from jsonplaceholder"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body'].replace("\n", "")
                })

post.csv
id","title","body"
1,"sunt aut facere repellat provident occaecati excepturi optio reprehenderit","quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totamnostrum rerum est autem sunt rem eveniet architecto"
...
100,"at nam consequatur ea labore ea harum","cupiditate quo est a modi nesciunt solutaipsa voluptas error itaque dicta inautem qui minus magnam et distinctio eumaccusamus ratione error aut"

## Task 3 : At the end of this exercise, students should be able to:

    Set up a basic web server using the http.server module.
    Handle different types of HTTP requests (GET, POST, etc.).
    Serve JSON data in response to specific endpoints.

task_02_http_server.py

#!/usr/bin/python3
"""
    Set up a basic web server using the http.server module.
    Handle different types of HTTP requests (GET, POST, etc.).
    Serve JSON data in response to specific endpoints.
"""
import http.server
import socketserver

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

info = {
    "version": "1.0",
    "description": "A simple API built with http.server"
    }


def webserver_basic():
    """basic webserver
    """
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler
    # Handler = BaseHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


class simpleHTTPServer(BaseHTTPRequestHandler):
    """class SimpleHTTPServer inherited from BaseHTTPRequestHandler
        duplicate the function of http.server.SimpleHTTPRequestHandler
    """
    def do_GET(self):
        """Handle HTTP GET request move to elif """
        # self.send_response(200)
        # send header
        # self.send_header("Content-Type", "application/json;charset=UTF-8")
        
        #self.end_headers()
        # response by stdout Hello ... 
        #self.wfile.write(b'Hello, this is a simple API!')
        
        # respond by stdout data in json format
        # json.dump(data, self.wfile) # has to be in post

        """Handle GET requests to parse url address"""
        parsed_path = urlparse(self.path)
        # parsed_path = self.path  # this work too without urllib.urlparse
        
        if parsed_path.path == '/data':
            # self.handle_json_data response()
            # print("endpoint /data parsed")
            # self.wfile.write(b"\nendpoint /data parsed")
            #self._json_data_response()
            self._json_data_response(data)

        elif parsed_path.path == '/info':
            # print('endpoint /info parased')
            # self.wfile.write(b"\nendpoint /info parsed")
            self._json_data_response(info)

        elif parsed_path.path == '/':  # root directory / main page
            self.send_response(200)
            # send header
            self.send_header("Content-Type", "text/plain; charset=UTF-8")
        
            self.end_headers()
            # response by stdout Hello ... 
            self.wfile.write(b'Hello, this is a simple API!')
        
        elif parsed_path.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=UTF-8")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=UTF-8")
            self.end_headers()
            # self.wfile.write(b"404 Not Found")  # checker issue
            self.wfile.write(b"Endpoint not found")  # checker issue          

    def _json_data_response(self, dataset):
        """You should return a simple dataset"""
        # self.wfile.write(b"OK")
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(dataset).encode("utf-8"))

httpd = HTTPServer(('', 8000), simpleHTTPServer)
httpd.serve_forever()

# webserver_basic()

## Task 4 : At the end of this exercise, students should be able to: 1. Set up a Flask application and run a development server. 2. Define and handle routes with Flask to respond to different endpoints. 3. Serve JSON data using Flask. 4. Understand the basics of request handling and response formation in Flask. 5. Handle POST requests to add new data to the API.

task_04_flask.py
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
    users[username] = {"username":user_data["username"], "name": user_data["name"],"age": user_data["age"], "city": user_data["city"]}
    # output = {"name": user_data["name"], "age": user_data["age"], "city": user_data["city"]}

    return jsonify({
        #"message": "User added", "user": output}), 201
        # "message": "User added", "user": user_data}), 200  # failed checker
        "message": "User added", "user": users[username]}), 201

if __name__ == '__main__':
    app.run(debug=True)




