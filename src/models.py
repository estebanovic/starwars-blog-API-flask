from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "people"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.JSON, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__ = "planets"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.JSON, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Starship(db.Model):
    __tablename__ = "starships"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.JSON, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Specie(db.Model):
    __tablename__ = "species"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.JSON, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    uid = db.Column(db.String, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    result = db.Column(db.JSON, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()