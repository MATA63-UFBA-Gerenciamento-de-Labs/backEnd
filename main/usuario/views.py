from . import usuario
from flask import request
from models import Usuario, Tipo
from main import db
from main.response import create_response


# Verificar autorização de RFID
@usuario.route("/atualizar", methods=["GET", "PUT"])
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
            200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso"
        )

    except Exception as e:
        print("Erro", e)
        return create_response(400, "usuario", {}, f"Erro ao atualizar cpf {body['cpf']}")

@usuario.route("/criar", methods=["POST"])
def criar_usuario():
    body = request.get_json()
    novo_usuario = Usuario()

    ultimo_usuario = Usuario.query.order_by(Usuario.id.desc()).first()
    ultimo_id = ultimo_usuario.id
    novo_usuario.id = str(int(ultimo_id) + 1)

    try:
        if "name" in body:
            novo_usuario.name = body["name"]
        if "senha" in body:
            novo_usuario.senha = body["senha"]
        if "email" in body:
            novo_usuario.email = body["email"]
        if "rf_id_code" in body:
            novo_usuario.rf_id_code = body["rf_id_code"]
        if "autorizado":
            novo_usuario.autorizado = body["autorizado"]
        if "cpf":
            novo_usuario.cpf = body["cpf"]
        if "tipo":
            novo_usuario.tipo = body["tipo"]



        db.session.add(novo_usuario)
        db.session.commit()

        return create_response(
            200, "usuario", novo_usuario.to_json(), "Criado com sucesso"
        )
    
    except Exception as e:
        print("Erro", e)
        return create_response(400, "usuario", {}, f"Erro ao cadastrar!")
