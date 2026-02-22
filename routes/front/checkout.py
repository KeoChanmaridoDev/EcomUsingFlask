from app import app, render_template

@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')