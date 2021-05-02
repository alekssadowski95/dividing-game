from flaskpackage import db

# Resets the database
db.drop_all()
db.create_all()