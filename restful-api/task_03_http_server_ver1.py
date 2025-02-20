#!/usr/bin/python3
"""
    Set up a basic web server using the http.server module.
    Handle different types of HTTP requests (GET, POST, etc.).
    Serve JSON data in response to specific endpoints.
"""
import http.server
import socketserver
import json

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

def do_GET():
    
    

