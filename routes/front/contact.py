from app import app, render_template

@app.get('/contact')
def contact():
    return render_template('front/contact.html', module='contact')