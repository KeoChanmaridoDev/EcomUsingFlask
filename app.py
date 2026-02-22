from flask import Flask, render_template, url_for

app = Flask(__name__)

import routes


if __name__ == '__main__':
    app.run()