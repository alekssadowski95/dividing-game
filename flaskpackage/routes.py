from flask import render_template, redirect, url_for
from flaskpackage import app, db
from flaskpackage.models import Note
from flaskpackage.forms import AddNoteForm
from sqlalchemy import desc


@app.route('/', methods=['GET'])
def home():
    # get all notes from the database and order by newest ones coming first
    notes = Note.query.order_by(desc(Note.id)).all()
    return render_template('home.html', notes=notes)

@app.route('/new', methods=['GET', 'POST'])
def add_note():
    form = AddNoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, text=form.text.data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add-note.html', title='New note', form=form)
