from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class Deadline(db.Model):
    __tablename__ = 'deadlines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date = db.Column(db.DateTime)

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)

