from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    """Read data from a JSON file and return as a list of dictionaries."""
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    """Read data from a CSV file and return as a list of dictionaries."""
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert 'id' and 'price' to appropriate types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Determine the data source and read data accordingly
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter by product_id if specified
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    # Render the template with product data
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
