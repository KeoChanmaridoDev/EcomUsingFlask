from app import app, render_template
import requests
import os


@app.get('/')
@app.get('/home')
def home():
    api_url = os.getenv('PRODUCTS_API_URL', 'https://fakestoreapi.com/products')
    products = []
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            # Normalize product shape for the frontend
            products = [
                {
                    'id': (item.get('id') or item.get('_id') or item.get('productId')),
                    'title': (item.get('title') or item.get('name') or ''),
                    'price': (item.get('price') or item.get('amount') or 0),
                    'img': (
                        item.get('img')
                        or item.get('image')
                        or item.get('thumbnail')
                        or item.get('picture')
                        or ''
                    ),
                    'description': (item.get('description') or item.get('desc') or item.get('short') or ''),
                }
                for item in data
                if isinstance(item, dict)
            ]
    except Exception:
        products = []

    return render_template('front/home.html', products=products, module='home')