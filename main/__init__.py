from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

PASSWORD = ""

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:{}@ep-autumn-dream-20888543.us-east-1.postgres.vercel-storage.com:5432/verceldb'.format(PASSWORD)
db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Hello World, from Flask!"


@app.route("/login")
def login():
    return "Login realizado"


# import and register Blueprints
from .aluno import aluno
app.register_blueprint(aluno, url_prefix='/aluno')