from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from config import DATABASE_CONNECTION_URI
from flask_marshmallow import Marshmallow

app= Flask(__name__)
app.secret_key= "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(contacts)
