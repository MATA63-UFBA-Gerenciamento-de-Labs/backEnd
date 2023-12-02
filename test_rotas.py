from main import app

USUARIO = {'id': 'teste', 'name': 'teste', 'rf_id_code': 'sample_id', 'autorizado': False}

def test_seleciona_usuarios_status_code():
    with app.test_client() as c:
        response = c.get('/aluno/usuarios')
        assert response.status_code == 200

def test_seleciona_usuarios_data():
    with app.test_client() as c:
        response = c.get('/aluno/usuarios')
        data = response.get_json()
        assert USUARIO in data["usuarios"]

def test_seleciona_usuario_existente():
    with app.test_client() as c:
        response = c.get('/aluno/usuarios')
        data = response.get_json()
        id_usuario = data["usuarios"][0]["id"]
        response = c.get('/aluno/usuario/'+str(id_usuario))
        data = response.get_json()
        assert len(data) == 1

def test_seleciona_usuario_inexistente():
    with app.test_client() as c:
        response = c.get('/aluno/usuario/inexistente')
        assert response.status_code == 500

def test_deleta_usuario_inexistente():
    with app.test_client() as c:
        response = c.delete('/aluno/usuario/inexistente')
        assert response.status_code == 400
