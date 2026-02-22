from app import app, render_template
from flask import request
import os 
import requests

@app.get('/details')
def details():
    # Get the product ID from the URL (like /details?id=5)
    product_id = request.args.get('id', '')
    
    # Get all products from the API
    api_url = os.getenv('PRODUCTS_API_URL', 'https://fakestoreapi.com/products')
    product = None
    
    try:
        # Ask the API to give us all products
        response = requests.get(api_url)
        products = response.json()
        
        # Look through all products to find the one that matches the ID
        for item in products:
            if isinstance(item, dict):
                # Get the product ID
                item_id = item.get('id')
                
                # Check if this is the product we're looking for
                if str(item_id) == str(product_id):
                    # Found it! Organize the product information
                    product = {
                        'id': item_id,
                        'title': item.get('title', ''),
                        'price': item.get('price', 0),
                        'description': item.get('description', ''),
                        'image': item.get('image', ''),
                        'category': item.get('category', ''),
                        'rating': item.get('rating', {}).get('rate', 0),
                        'rating_count': item.get('rating', {}).get('count', 0),
                    }
                    break
        
        # If we couldn't find the product, create a default one
        if not product:
            product = {
                'id': 0,
                'title': 'Product not found',
                'price': 0,
                'description': 'This product does not exist.',
                'image': '',
                'category': '',
                'rating': 0,
                'rating_count': 0,
            }
    
    except Exception as e:
        # If something goes wrong, create a default product
        product = {
            'id': 0,
            'title': 'Error loading product',
            'price': 0,
            'description': 'Could not load product information.',
            'image': '',
            'category': '',
            'rating': 0,
            'rating_count': 0,
        }
    
    # Send the product information to the HTML page
    return render_template('front/productDetails.html', product=product)