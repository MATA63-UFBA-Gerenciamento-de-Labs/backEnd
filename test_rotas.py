import unittest
from unittest.mock import MagicMock
import json
from main import app
from models import Usuario

class UsuarioRouteCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.db = MagicMock()

        self.app_context = self.app.app_context()
        self.app_context.push()

        self.db.create_all()
        self.sample_usuario = Usuario(id="teste", name="teste", rf_id_code="sample_id", autorizado=False)
        self.db.session.add(self.sample_usuario)
        self.db.session.commit()

    def tearDown(self):

        self.app_context.pop()

    def test_seleciona_usuarios(self):
        self.db.session.query.return_value.filter.return_value.all.return_value = [self.sample_usuario]

        with self.app.app_context():
            self.app.extensions['sqlalchemy'].db = self.db

            response = self.client().get("/aluno/usuarios")
            data = response.json 

            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 1)

if __name__ == "__main__":
    unittest.main()