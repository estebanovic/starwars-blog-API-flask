from datetime import datetime
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "people"
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    # planets = db.relationship('Planet', cascade='all, delete', backref='user')

    def serialize(self):
        return {
            "uid" : self.uid,
            "message" : self.message,
            "description" : self.description,
            "_id" : self._id,
            "__v" : self._v,
            "height" : self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "created" : self.created,
            "edited" : self.edited,
            "name" : self.name,
            "url" : self.url,
            # "planets" : self.get_planets()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def get_planets(self):
    #     planets = list(map(lambda planet: planet.serialize(), self.planets))
    #     return planets


class Planet(db.Model):
    __tablename__ = "planets"
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    # person_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

    def serialize(self):
        return {
            "uid" : self.uid,
            "message" : self.message,
            "description" : self.description,
            "_id" : self._id,
            "__v" : self._v,
            "diameter" : self.diameter,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "gravity" : self.gravity,
            "population" : self.population,
            "climate" : self.climate,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "created" : self.created,
            "edited" : self.edited,
            "name" : self.name,
            "url" : self.url,
        }

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
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    starship_class = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    cost_in_credits = db.Column(db.String, nullable=False)
    length = db.Column(db.String, nullable=False)
    crew = db.Column(db.String, nullable=False)
    passengers = db.Column(db.String, nullable=False)
    max_atmosphering_speed = db.Column(db.String, nullable=False)
    hyperdrive_rating = db.Column(db.String, nullable=False)
    MGLT = db.Column(db.String, nullable=False)
    cargo_capacity = db.Column(db.String, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    created = db.Column(db.DATE, nullable=False)
    edited = db.Column(db.DATE, nullable=False)
    name = db.Column(db.String, nullable=False)
    ulr = db.Column(db.String, nullable=False)
    #TODO PILOTS

    def serialize(self):
        return {
            "uid" : self.uid,
            "message" : self.message,
            "description" : self.description,
            "_id" : self._id,
            "__v" : self._v,
            "model" : self.model,
            "starship_class" : self.starship_class,
            "manufacturer" : self.manufacturer,
            "cost_in_credits" : self.cost_in_credits,
            "length" : self.length,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "hyperdrive_rating" : self.hyperdrive_rating,
            "MGLT" : self.MGLT,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables,
            "created" : self.created,
            "edited" : self.edited,
            "name" : self.name,
            "ulr" : self.ulr
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def get_pilots(self):
    #     pilots = list(map(lambda pilot: pilot.serialize(), self.pilots))
    #     return pilots


class Specie(db.Model):
    __tablename__ = "species"
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    classification = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    average_height = db.Column(db.Integer, nullable=False)
    average_lifespan = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    lenguaje = db.Column(db.String, nullable=False)
    created = db.Column(db.DATE, nullable=False)
    edited = db.Column(db.DATE, nullable=False)
    name = db.Column(db.String, nullable=False)
    ulr = db.Column(db.String, nullable=False)
    #TODO PLANETS
    #TODO PEOPLE

    def serialize(self):
        return {
            "uid" : self.uid,
            "message" : self.message,
            "description" : self.description,
            "_id" : self._id,
            "__v" : self._v,
            "classification" : self.classification,
            "designation" : self.designation,
            "average_height" : self.average_height,
            "average_lifespan" : self.average_lifespan,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "lenguaje" : self.lenguaje,
            "created" : self.created,
            "edited" : self.edited,
            "name" : self.name,
            "ulr" : self.ulr
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    # def get_people(self):
    #     people = list(map(lambda person: person.serialize(), self.people))
    #     return people


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    vehicle_class = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    cost_in_credits = db.Column(db.String, nullable=False)
    length = db.Column(db.String, nullable=False)
    crew = db.Column(db.String, nullable=False)
    passengers = db.Column(db.String, nullable=False)
    max_atmosphering_speed = db.Column(db.String, nullable=False)
    cargo_capacity = db.Column(db.String, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    created = db.Column(db.DATE, nullable=False)
    edited = db.Column(db.DATE, nullable=False)
    name = db.Column(db.String, nullable=False)
    ulr = db.Column(db.String, nullable=False)
    #TODO FILS
    #TODO PILOTS

    def serialize(self):
        return {
            "uid" : self.uid,
            "message" : self.message,
            "description" : self.description,
            "_id" : self._id,
            "__v" : self._v,
            "model" : self.model,
            "vehicle_class" : self.vehicle_class,
            "manufacturer" : self.manufacturer,
            "cost_in_credits" : self.cost_in_credits,
            "length" : self.length,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables,
            "created" : self.created,
            "edited" : self.edited,
            "name" : self.name,
            "ulr" : self.ulr
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def get_films(self):
    #     films = list(map(lambda film: film.serialize(), self.films))
    #     return films

    # def get_pilots(self):
    #     pilots = list(map(lambda pilot: pilot.serialize(), self.pilots))
    #     return pilots


class Film(db.Model):
    __tablename__ = "films"
    uid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    _id = db.Column(db.String, nullable=False)
    _v = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    episode_id = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String, nullable=False)
    opening_crawl = db.Column(db.String, nullable=False)
    created = db.Column(db.DATE, nullable=False)
    edited = db.Column(db.DATE, nullable=False)
    name = db.Column(db.String, nullable=False)
    ulr = db.Column(db.String, nullable=False)
    # people = db.relationship('Person', cascade='all, delete', backref='contact')
    # planets = db.relationship('Planet', cascade='all, delete', backref='contact')
    # starships = db.relationship('Starship', cascade='all, delete', backref='contact')
    # vehicles = db.relationship('Vehicle', cascade='all, delete', backref='contact')
    # species = db.relationship('Specie', cascade='all, delete', backref='contact')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def get_people(self):
    #     people = list(map(lambda person: person.serialize(), self.people))
    #     return people

    # def get_planets(self):
    #     planets = list(map(lambda planet: planet.serialize(), self.planets))
    #     return planets

    # def get_starships(self):
    #     starships = list(map(lambda starship: starship.serialize(), self.starships))
    #     return starships

    # def get_vehicles(self):
    #     vehicles = list(map(lambda vehicle: vehicle.serialize(), self.vehicles))
    #     return vehicles

    # def get_species(self):
    #     species = list(map(lambda specie: specie.serialize(), self.peopspeciesle))
    #     return species

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    #TODO list of favorites

    def serialize(self):
        return {
            "id" : self.id,
            "firs_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "password" : self.password
            #TODO list of favorites
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    favorite_uid = db.Column(db.String, nullable=False)
    favorite_class = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "id" : self.id,
            "favorite_uid" : self.favorite_uid,
            "favorite_class" : self.favorite_class
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
