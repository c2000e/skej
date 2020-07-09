import datetime

from app import db

def status_default(context):
    if context.get_current_parameters()['date'] < datetime.datetime.today():
        return 'past due'
    return 'in progress'

class DeadlineModel(db.Model):
    __tablename__ = 'deadlines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    status = db.Column(db.String(32), default=status_default)

    def __init__(self, name, date, status=None):
        self.name = name
        self.date = date
        self.status = status

