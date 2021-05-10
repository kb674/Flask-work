from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# Changed to SQLite for github for security reasons
app.config["SECRET_KEY"] = ""
# Same for the secret key

db = SQLAlchemy(app)

from application import routes