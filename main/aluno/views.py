from . import aluno
from flask import request
from models import Usuario, Tipo
from main import db
from main.response import create_response


# Selecionar Tudo
@aluno.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.filter_by(tipo=Tipo.aluno).all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    return create_response(200, "usuarios", usuarios_json)


# Selecionar Individual
@aluno.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return create_response(200, "usuario", usuario_json)


# Verificar autorização de RFID
@aluno.route("/autorizado/", methods=["GET"])
def autorizacao_usuario():
    id_request = request.args.get("rf_id_code").replace("+", "-").replace(" ", "-")
    usuario_objeto = (
        Usuario.query.filter_by(rf_id_code=id_request)
        .with_entities(Usuario.autorizado)
        .first()
    )

    if usuario_objeto:
        authorized_value = usuario_objeto[0]
        if authorized_value is True:
            return create_response(200, "autorizado", "true")
        else:
            return create_response(200, "autorizado", "false")
    else:
        return create_response(
            404, "error", "RFID nao encontrado: {}".format(id_request)
        )


# Atualizar
@aluno.route("/change/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if "autorizado" in body:
            usuario_objeto.autorizado = body["autorizado"]

        db.session.add(usuario_objeto)
        db.session.commit()
        return create_response(
            200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso"
        )
    except Exception as e:
        print("Erro", e)
        return create_response(400, "usuario", {}, "Erro ao atualizar")


# Deletar
@aluno.route("/usuario/<id>", methods=["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return create_response(
            200, "usuario", usuario_objeto.to_json(), "Deletado com sucesso"
        )
    except Exception as e:
        print("Erro", e)
        return create_response(400, "usuario", {}, "Erro ao deletar")
