from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import os
import random

app = Flask(__name__)
CORS(app)  # Enable CORS

# Dynamic file path for laptops_data.json
DATA_FILE = os.path.join(os.path.dirname(__file__), 'laptops_data.json')

# Load laptop data from the JSON file
try:
    with open(DATA_FILE, 'r') as file:
        laptops_data = json.load(file)
except FileNotFoundError:
    laptops_data = []
    print(f"Error: {DATA_FILE} not found.")

# Helper function to parse price
def parse_price(price_str):
    """Convert price string to a float."""
    try:
        return float(price_str.replace(',', '').strip())
    except ValueError:
        return None  # Return None if the price cannot be parsed

# Helper function to filter laptops based on parameters
def filter_laptops(data, filters):
    filtered_data = data

    if 'category' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['category'].lower() in laptop['Category'].lower()]

    if 'source' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['source'].lower() in laptop['Source'].lower()]

    if 'price_less_than' in filters:
        try:
            max_price = float(filters['price_less_than'])
            filtered_data = [laptop for laptop in filtered_data if parse_price(laptop['Price']) and parse_price(laptop['Price']) < max_price]
        except ValueError:
            pass

    if 'price_greater_than' in filters:
        try:
            min_price = float(filters['price_greater_than'])
            filtered_data = [laptop for laptop in filtered_data if parse_price(laptop['Price']) and parse_price(laptop['Price']) > min_price]
        except ValueError:
            pass

    if 'rating_greater_than' in filters:
        try:
            filtered_data = [laptop for laptop in filtered_data if float(laptop['Rating'].split()[0]) > float(filters['rating_greater_than'])]
        except ValueError:
            pass

    if 'rating_less_than' in filters:
        try:
            filtered_data = [laptop for laptop in filtered_data if float(laptop['Rating'].split()[0]) < float(filters['rating_less_than'])]
        except ValueError:
            pass

    if 'deal' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['deal'].lower() in laptop['Deal Available'].lower()]

    if 'limit' in filters:
        try:
            limit = int(filters['limit'])
            filtered_data = filtered_data[:limit]
        except ValueError:
            pass

    return filtered_data

# Route for the home page with modern guide
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all laptops with filtering
@app.route('/laptops', methods=['GET'])
def get_laptops():
    filters = request.args
    filtered_laptops = filter_laptops(laptops_data, filters)
    return jsonify(filtered_laptops)

# Route to get a random laptop
@app.route('/laptop/random', methods=['GET'])
def get_random_laptop():
    random_laptop = random.choice(laptops_data)
    return jsonify(random_laptop)

if __name__ == '__main__':
    app.run(debug=True)
