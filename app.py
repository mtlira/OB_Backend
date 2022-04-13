from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config.env_load import *
from routes.blueprint import bp

app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = SECRET_KEY
app.config['CORS_HEADERS'] = CORS_HEADERS
app.register_blueprint(bp, url_prefix = "/mangobank-back")
db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()
    if TEST_MODE == 'ON': app.run(debug=True)
    else: app.run(host='0.0.0.0', port=80, debug = True)