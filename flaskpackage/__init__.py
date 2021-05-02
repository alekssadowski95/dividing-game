from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Sets up the application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kljpafmuvsncse:05f94971e593aebd3b2faad889ee12d6cfef0bdad0df1121f4ec58e112ceb9a7@ec2-54-216-48-43.eu-west-1.compute.amazonaws.com:5432/d5g90uhkjd4sml'
app.config['SECRET_KEY'] = '59f063a2e5406614813c5b07e129fdeb'
db = SQLAlchemy(app)

from flaskpackage import routes