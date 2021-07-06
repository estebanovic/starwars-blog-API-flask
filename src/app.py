from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import  db, Person, Planet

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
db.init_app(app)
Migrate(app, db)