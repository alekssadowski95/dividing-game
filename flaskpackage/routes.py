from flask import render_template, redirect, url_for
from flaskpackage import app, db
from flaskpackage.models import Note
from flaskpackage.forms import AddNoteForm
from sqlalchemy import desc


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

