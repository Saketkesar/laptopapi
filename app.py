from flask import Flask, jsonify, request
import json
import random
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)

# Load laptop data from the JSON file
with open('laptops_data.json', 'r') as file:
    laptops_data = json.load(file)

# Helper function to filter data based on parameters
def filter_laptops(data, filters):
    filtered_data = data

    # Apply filters based on the provided parameters
    if 'category' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['category'].lower() in laptop['Category'].lower()]

    if 'source' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['source'].lower() in laptop['Source'].lower()]

    if 'price_less_than' in filters:
        filtered_data = [laptop for laptop in filtered_data if float(laptop['Price'].replace(',', '').replace('₹', '').strip()) < float(filters['price_less_than'])]

    if 'price_greater_than' in filters:
        filtered_data = [laptop for laptop in filtered_data if float(laptop['Price'].replace(',', '').replace('₹', '').strip()) > float(filters['price_greater_than'])]

    if 'rating_greater_than' in filters:
        filtered_data = [laptop for laptop in filtered_data if float(laptop['Rating'].split()[0]) > float(filters['rating_greater_than'])]

    if 'rating_less_than' in filters:
        filtered_data = [laptop for laptop in filtered_data if float(laptop['Rating'].split()[0]) < float(filters['rating_less_than'])]

    if 'deal' in filters:
        filtered_data = [laptop for laptop in filtered_data if filters['deal'].lower() in laptop['Deal Available'].lower()]

    # Apply limit filter
    if 'limit' in filters:
        try:
            limit = int(filters['limit'])
            filtered_data = filtered_data[:limit]
        except ValueError:
            pass  # If invalid value, return as is

    return filtered_data

# Route for the home page (UI/UX with guide)
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all laptop data
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
