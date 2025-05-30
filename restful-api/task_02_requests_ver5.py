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
    count = 1  # API valid ID (1- 100)
    url = f"https://jsonplaceholder.typicode.com/posts/{count}"
    quote ='"'

    print("Please wait\n")
    # response = requests.get(url, timeout=3)
    response = requests.get(url, timeout=10)
    # response = requests.head(url)
    # print(response)
    # print(f"Status Code: {response.status_code}") for debugging
    # result_dict = {}
    result_list = []
    while response:
        if response:
            # print(response)  # for debugging
            # print(response.json())
            API_data = response.json()
            # print(API_data)
            # print(API_data['title'])  # for debugging
            
            # my_dict = {'id': API_data['id'], 'title': API_data['title'], 'body': API_data['body']}
            # my_dict = {'id':API_data['id'], 'title':API_data['title'], 'body':API_data['body']}
            # student_details = json.loads(jsonString)
            # my_dict = json.loads(API_data)
            my_dict = {
                        "id": API_data.get('id', None),  # Fallback to `None` if missing
                        "title": API_data.get('title', " "),
                        "body": API_data.get('body', " ")
                        }

            # result_dict.append({my_dict})
            # result_dict.update({my_dict})


            result_list.append(my_dict)
            # print(my_dict)  # for debugging  
        else:
            raise Exception(f"{response.status_code}")
        count += 1
        url = f"https://jsonplaceholder.typicode.com/posts/{count}"
        # response = requests.get(url, timeout=3)
        response = requests.get(url, timeout=10)
    # print(result_dict)  # for debugging
    # print(result_list)  # for debugging
    with open(file_name, 'w', newline="") as file:
        # writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'], quotechar='"',
        #    quoting=csv.QUOTE_NONNUMERIC)
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'], quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        
        writer.writeheader()
        writer.writerows(result_list)
        # writer.writerow(result_list)
        
    # pass
