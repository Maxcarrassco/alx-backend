#!/usr/bin/env python3
"""ALX SE Backend I18N."""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Configuration for babel."""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """Render hello world in the browser."""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
