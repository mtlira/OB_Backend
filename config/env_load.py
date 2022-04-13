import os
from dotenv import load_dotenv

load_dotenv()

TEST_MODE = os.environ.get('TEST_MODE')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_LOCAL') if TEST_MODE == 'ON' else os.environ.get('SQLALCHEMY_DATABASE_URI_CLOUD')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
SECRET_KEY = os.environ.get('SECRET_KEY')
CORS_HEADERS = os.environ.get('CORS_HEADERS')
BASIC_APP_URL = os.environ.get('BASIC_APP_URL')