from flaskpackage import db
from datetime import datetime


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(32), nullable=False)
    score = db.Column(db.Integer(), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    played_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Score("{self.uuid}","{self.score}","{self.nickname}", "{self.played_date}")'