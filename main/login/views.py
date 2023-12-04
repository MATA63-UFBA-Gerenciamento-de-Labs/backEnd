from models import Usuario
from . import login
from flask import request
from main.response import create_response


@login.route("/", methods=["GET"])
def login():
    try:
        # Access query parameters using request.args
        received_cpf = request.args.get("cpf")
        received_password = request.args.get("password")

        # Check if user exists
        user = Usuario.query.filter_by(cpf=received_cpf).first()

        if user and user.senha == received_password:
            return create_response(200, "response", user.to_json())
        else:
            return create_response(401, "response", "unauthorized")
    except Exception as e:
        return create_response(500, "response", f"Error: {e}")
