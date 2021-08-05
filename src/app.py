from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import  User, db, Person, Planet

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
db.init_app(app)
Migrate(app, db)

@app.route('/people', methods=['GET','POST'])
@app.route('/people/<int:id>', methods=['GET','POST'])
def people(id=None):

    if request.method == 'GET':
        if id != None:
            person = Person.query.get(id)
            return jsonify(person.serialize()), 200

        people = Person.query.all()
        people = list(map(lambda person: person.serialize(), people))
        return jsonify(people), 200

    if request.method == 'POST':

        uid = request.json.get('uid')
        message = request.json.get('message')
        description = request.json.get('description')
        _id = request.json.get('_id')
        _v = request.json.get('__v')
        height = request.json.get('height')
        mass = request.json.get('mass')
        hair_color = request.json.get('hair_color')
        skin_color = request.json.get('skin_color')
        eye_color = request.json.get('eye_color')
        birth_year = request.json.get('birth_year')
        gender = request.json.get('gender')
        created = request.json.get('created')
        edited = request.json.get('edited')
        name = request.json.get('name')
        url = request.json.get('url')

        person = Person()
        person.uid = uid
        person.message = message
        person.description = description
        person._id = _id
        person._v = _v
        person.height = height
        person.mass = mass
        person.hair_color = hair_color
        person.skin_color = skin_color
        person.eye_color = eye_color
        person.birth_year = birth_year
        person.gender = gender
        person.created = created
        person.edited = edited
        person.name = name
        person.url = url

        person.save()

        return jsonify(person.serialize()), 201


@app.route('/planets', methods=['GET','POST'])
@app.route('/planets/<int:id>', methods=['GET','POST'])
def planets(id=None):

    if request.method == 'GET':
        if id != None:
            planet = Planet.query.get(id)
            return jsonify(planet.serialize()), 200

        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify(planets), 200

    if request.method == 'POST':

        uid = request.json.get('uid')
        message = request.json.get('message')
        description = request.json.get('description')
        _id = request.json.get('_id')
        _v = request.json.get('__v')
        diameter = request.json.get('diameter')
        rotation_period = request.json.get('rotation_period')
        orbital_period = request.json.get('orbital_period')
        gravity = request.json.get('gravity')
        population = request.json.get('population')
        climate = request.json.get('climate')
        terrain = request.json.get('terrain')
        surface_water = request.json.get('surface_water')
        created = request.json.get('created')
        edited = request.json.get('edited')
        name = request.json.get('name')
        url = request.json.get('url')

        planet = Planet()
        planet.uid = uid
        planet.message = message
        planet.description = description
        planet._id = _id
        planet._v = _v
        planet.diameter = diameter
        planet.rotation_period = rotation_period
        planet.orbital_period = orbital_period
        planet.gravity = gravity
        planet.population = population
        planet.climate = climate
        planet.terrain = terrain
        planet.surface_water = surface_water
        planet.created = created
        planet.edited = edited
        planet.name = name
        planet.url = url

        planet.save()

        return jsonify(planet.serialize()), 201


@app.route('/users', methods=['GET','POST'])
@app.route('/users/<int:id>', methods=['GET','POST'])
def users(id=None):
    
    if request.method == 'GET':
        if id != None:
            user = User.query.get(id)
            return jsonify(user.serialize()), 200
        
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))
        return jsonify(users), 200

    if request.method == 'POST':
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email = request.json.get('email')
        password = request.json.get('password')

        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password

        user.save()

        return jsonify(user.serialize()), 201

if __name__ == '__main__':
    app.run()