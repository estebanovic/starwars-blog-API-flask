from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class People(db.Model):
    __tablename__ = "people"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.Json, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()