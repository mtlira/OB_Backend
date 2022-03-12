from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config
from routes.blueprint import bp

app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = config.SECRET_KEY
app.config['CORS_HEADERS'] = config.CORS_HEADERS
app.register_blueprint(bp)
db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()        
    app.run(debug = True)