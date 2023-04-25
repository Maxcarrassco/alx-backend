#!/usr/bin/env python3
"""ALX SE Backend I18N."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Mapping


class Config(object):
    """Configuration for babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Return the best match of locale to use."""
    locale = request.query_string.decode()
    if locale:
        return locale.split('=')[-1]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def get_user():
    """Return a dict of user info or None."""
    param = request.query_string.decode()
    if not param:
        return None
    user_id = int(param.split('=')[-1])
    user = users.get(user_id)
    if user:
        g.user = user
    return user


@app.route('/')
def index():
    """Render hello world in the browser."""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run()
