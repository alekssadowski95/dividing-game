from flaskpackage import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Note("{self.title}","{self.text}")'