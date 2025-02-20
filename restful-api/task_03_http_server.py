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

"""basic webserver"""
def webserver_basic():
    
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
        """Handle HTTP GET request"""
        self.send_response(200)
        # send header
        # self.send_header("Content-Type", "application/json;charset=UTF-8")
        
        self.end_headers()
        # response by stdout Hello ... 
        self.wfile.write(b'Hello, this is a simple API!')
        # respond by stdout data in json format
        # json.dump(data, self.wfile) # has to be in post

        """Handle GET requests to parse url address"""
        parsed_path = urlparse(self.path)
        
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

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"\nEndpoint not found\n")

    def _json_data_response(self, dataset):
        """You should return a simple dataset"""
        self.wfile.write(b"\nOK\n")
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(dataset).encode())

httpd = HTTPServer(('', 8000), simpleHTTPServer)
httpd.serve_forever()

# def main():
# webserver_basic()   

