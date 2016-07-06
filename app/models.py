from app import db
import datetime


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    status = db.Column(db.Integer, default=0)

