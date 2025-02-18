#!/usr/bin/python3
"""Consuming and processing data from an API using Python 
"""
import requests


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

    pass
    