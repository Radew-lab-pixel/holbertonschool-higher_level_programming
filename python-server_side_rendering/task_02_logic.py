#!/usr/bin/python3

from flask import Flask, render_template
import json

app = Flask(__name__)

# static module for loading json file
def read_file():
    filename = "items.json"
    with open(filename, "r") as f:
        data = json.load(f)
    if data:
        return data['items']  # return dict values (alist) of key items
    else:
        empty_data=[]
        return empty_data
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_list = read_file()
    # if items_list is None:
    #    items_list = []
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)