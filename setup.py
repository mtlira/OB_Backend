from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_user:user123@localhost/db_inovadora'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user123@localhost/db_inovadora'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['CORS_ORIGINS'] = ['http://127.0.0.1']

db = SQLAlchemy(app)