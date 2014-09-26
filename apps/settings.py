import os

# from secret_keys import CSRF_SECRET_KEY, SESSION_KEY
"""
settings.py

Configuration for Flask app

"""
from datetime import timedelta

class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "sooyeon.song222@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///Atelier?instance=likeliondb:like'
    migration_directory = 'migrations'

