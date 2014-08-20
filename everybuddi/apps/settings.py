"""
settings.py

Configuration for Flask app

"""
import os
from datetime import timedelta


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "astyfx@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=baeggot-personal-project:ll-personal-blog'
    migration_directory = 'migrations'







