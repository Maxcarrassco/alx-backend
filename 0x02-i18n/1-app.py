#!/usr/bin/env python3
"""ALX SE Backend I18N."""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for babel."""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    """Render hello world in the browser."""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
