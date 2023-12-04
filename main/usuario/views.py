from . import usuario
from flask import request
from models import Usuario, Tipo
from main import db
from main.response import create_response


# Verificar autorização de RFID
@usuario.route("/atualizar", methods=["GET","PUT"])
def atualizar_dados_usuario():
    body = request.get_json()

    try:
        usuario_objeto = Usuario.query.filter_by(cpf=body["cpf"]).first()
    except Exception as e:
        print("Erro", e)
        return create_response(400, "CPF Não encontrado")

    try:
        if "name" in body:
            usuario_objeto.name = body["name"]
        if "senha" in body:
            usuario_objeto.senha = body["senha"]
        if "email" in body:
            usuario_objeto.email = body["email"]


        db.session.add(usuario_objeto)
        db.session.commit()

        return create_response(
            400, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso"
        )
    
    except Exception as e:
        print("Erro", e)
        return create_response(400, "usuario", {}, f"Erro ao atualizar cpf {body['cpf']}")

