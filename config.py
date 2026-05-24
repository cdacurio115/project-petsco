import os
from dotenv import load_dotenv

load_dotenv()

class config:
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class productionconfig(config):
    debug = False

class developmentconfig(config):
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")