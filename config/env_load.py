import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
SECRET_KEY = os.environ.get('SECRET_KEY')
CORS_HEADERS = os.environ.get('CORS_HEADERS')

print('DATABASE URI:',SQLALCHEMY_DATABASE_URI)