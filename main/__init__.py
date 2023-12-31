from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

PASSWORD = os.environ.get("POSTGRES_PASSWORD")

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:{}@ep-autumn-dream-20888543.us-east-1.postgres.vercel-storage.com:5432/verceldb'.format(PASSWORD)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://default:{}@ep-autumn-dream-20888543.us-east-1.postgres.vercel-storage.com:5432/verceldb".format(PASSWORD)
CORS(app)
db = SQLAlchemy(app)


@app.route("/")
def home():
    return "Hello World, from Flask!"


# import and register Blueprints
from .aluno import aluno
from .login import login
from .usuario import usuario

app.register_blueprint(aluno, url_prefix="/aluno")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(usuario, url_prefix="/usuario")
