from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '59f063a2e5406614813c5b07e129fdeb'
db = SQLAlchemy(app)

from flaskpackage import routes