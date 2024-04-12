#!/usr/bin/env python3
"""Defining A Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Languages Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """gets the best language match"""
    # Locale from URL parameters
    locale_lang = request.args.get('locale')
    if locale_lang and locale_lang in Config.LANGUAGES:
        return locale_lang

    # Locale from user settings
    if hasattr(g, 'user') and g.user:
        users_lang = g.user.get('locale')
        if users_lang and users_lang in Config.LANGUAGES:
            return users_lang

    # Locale from request header
    best_match = request.accept_languages.best_match(Config.LANGUAGES)
    if best_match:
        return best_match

    # Default locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route('/')
def index():
    """Root route"""
    username = None
    if hasattr(g, 'user') and g.user:
        username = g.user.get('name')
    return render_template('7-index.html',
                           username=username)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a dictionay of a user if users_id exists
    and was passed in the request arguments"""
    users_id = request.args.get('login_as')
    if users_id:
        user = users.get(int(users_id))
        if user:
            return user
    return None


@app.before_request
def before_request():
    """sets globally the user if found"""
    user = get_user()
    if user:
        g.user = user


@babel.timezoneselector
def get_timezone():
    """gets best match timezone"""
    # Timezone from URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            timezone(url_timezone)
            return timezone(url_timezone)
        except UnknownTimeZoneError:
            print(f"Invalid timezone: {url_timezone}")

    # Timezone from users settings
    if hasattr(g, 'user') and g.user:
        users_timezone = g.user.get('timezone')
        if users_timezone:
            try:
                timezone(users_timezone)
                return timezone(users_timezone)
            except UnknownTimeZoneError:
                print(f"Invalid timezone: {users_timezone}")

    # Timezone from defualt timezone
    default_timezone = Config.BABEL_DEFAULT_TIMEZONE
    return timezone(default_timezone)


if __name__ == '__main__':
    app.run(debug=True)
