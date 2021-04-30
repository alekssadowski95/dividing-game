from flaskpackage import db
from flaskpackage.models import Note


'''
WARNING: THIS WILL DELETE ALL DATA FROM THE DATABASE!
'''
db.drop_all()
db.create_all()

init_note = Note(title='Initial note', text='This is the initial note. It gets created automatically, when the database is initialized')
db.session.add(init_note)

db.session.commit()