#!/usr/bin/python3


from flask import Flask, render_template
import json
import os, csv

app = Flask(__name__)

def read_json_file():
    filename = "products.json"
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

      # Ensure we have a list of products
            if isinstance(data, list):
                return data
            return None
    except (json.JSONDecodeError, FileNotFoundError):
        return None
"""            
            return data
    except (json.JSONDecodeError, FileExistsError):
        return None
"""
def read_csv_file():
    """Read and parse products from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None



# @app.route('/products')
@app.route('/products/<string:data_source>')
@app.route('/products/<string:data_source>/<int:product_id>')
# def products(data_source, product_id=None):
def products(data_source):
    # source = request.args.get('source', '').lower() too complicated
    data_source = data_source.lower()
    # if data_source not in ("json", "csv"):
    if data_source == 'json':
        products_list = read_json_file()
    elif data_source == 'csv':
        products_list = read_csv_file()
    else:
        return render_template('product_display.html', error = f"Wrong source as it {data_source}")

    if products_list is None:
        return render_template('product_display.html', error = f"Error with source {data_source}")
    else:
        return render_template('product_display.html', products = products_list)

if __name__ == "__main__":
     app.run(debug=True, port=5000)