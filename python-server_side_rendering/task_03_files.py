#!/usr/bin/python3


from flask import Flask, render_template, request
import json
import os
import csv

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
def read_csv_file():
        products = []
    # required_fields = {'id', 'name', 'category', 'price'}
    
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Verify all required fields are present
            # if not required_fields.issubset(reader.fieldnames):
            #    print("Missing required fields in CSV")
            
            #    return None
                
            for row_num, row in enumerate(reader, 1):
                try:
                    # Validate and convert fields
                    product = {
                        'id': int(row['id']),
                        'name': row['name'].strip(),
                        'category': row['category'].strip(),
                        'price': float(row['price'])
                    }
                    print(product['id'])
                    # Basic data validation
                    if product['id'] <= 0:
                        raise ValueError("ID must be positive")
                    if product['price'] < 0:
                        raise ValueError("Price cannot be negative")
                        
                    products.append(product)
                    
                except (ValueError, KeyError) as e:
                    print(f"Skipping row {row_num}: {str(e)}")
                    continue
                    
        return products if products else None
        
    except FileNotFoundError:
        print("CSV file not found")
        return None
    except Exception as e:
        print(f"Unexpected error reading CSV: {str(e)}")
        return None
"""
"""
def read_csv_file():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            print(reader)
            for row in reader:
                print(row)
                # Convert price to float and id to int
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
              
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None
"""      

"""
def read_json_file():
    filename = "products.json"
    with open(filename, 'r') as f:
        return json.load(f)
"""

def read_csv_file():
    products = []
    filename = "products.csv"
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        # print(reader)
        for row in reader:
            # row['id'] = int(row['id'])
            # row['price'] = float(row['price'])
            product = {
                        'id': int(row['id']),
                        'name': row['name'].strip(),
                        'category': row['category'].strip(),
                        'price': float(row['price'])
                        }
            
            products.append(product)
    return products

def filter_id(product_id, products):
    # for product in products:
        # print(f"row{product}")
    #    if product['id'] == int(product_id):
            # return product
        # if product.id == int(product_id):
    #
    # 
    # filtered_products = [p for p in products if p['id'] == product_id]
    """
    for product in products:
        # if (product["id"] == int(product_id)):
        if product.get("id") == int(product_id):
    # if filtered_products:
    #    print(filtered_products)
            print(product["name"])
            return render_template('product_display.html', products = product)
    # print(product)
    return render_template('product_display.html', error = "Product not found")
    """
def filter_id(product_id, products):
    try:
        pid = int(product_id)
        filtered = [p for p in products if p.get("id") == pid]
        if filtered:
            return render_template('product_display.html', product=filtered[0])
    except ValueError:
        pass
    return render_template('product_display.html', error="Product not found")



@app.route('/products')
def display_products():
    data_source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    
    # Read data based on source
    if data_source == 'json':
        products = read_json_file()
        # print(products)
        # data_source = 'JSON'
    
    elif data_source == 'csv':
        products = read_csv_file()
        # print(products)
        # data_source = 'CSV'
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        filter_id(product_id, products)


    
    # Check if data was loaded successfully
    if products is None:
        return render_template('product_display.html', 
                             error=f"Error loading {data_source} data.")

    return render_template('product_display.html',products=products)
    
    """
    # Handle empty results (valid for ID filtering)
    if not products:
        return render_template('product_display.html',
                            error="Product not found.")
    else:
        return render_template('product_display.html',products=products)
    """

"""
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
"""

if __name__ == "__main__":
     app.run(debug=True, port=5000)