#!/usr/bin/python3
"""Consuming and processing data from an API using Python 
"""
import requests


def fetch_and_print_posts():
    """method to fetch and print posts from jsonplaceholder""" 
    response = requests.get("https://jsonplaceholder.typicode.com/posts/") # for debugging
    # response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response:
        # print(response)  # for debugging
        # print(response.json())
        API_data = response.json()
        for key in API_data:
              # print(key)  # for debugging
              # print(value)  # for debugging
              if key == "title":
                # print(f"{API_data[key]}")
                print(API_data[key])
                # pass      
    else:
        raise Exception(f"{response.status_code}")

def fetch_and_save_posts():
    pass
    