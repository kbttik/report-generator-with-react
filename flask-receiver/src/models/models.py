from datetime import datetime
from src.database import db


class Report(db.Model):

    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, title, url, dt=datetime.now):
        self.title = title
        self.url = url
        # self.created_at = dt

class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    id_report = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(50), nullable=False)

    def __init__(self, id_report, tag):
        self.id_report = id_report
        self.tag = tag
