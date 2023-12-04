from main import db
import enum


class Tipo(enum.Enum):
    aluno = 0
    professor = 1
    tecnico = 2


# models
class Usuario(db.Model):
    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(50))
    rf_id_code = db.Column(db.String(11))
    autorizado = db.Column(db.Boolean())
    cpf = db.Column(db.String(11))
    tipo = db.Column(db.Enum(Tipo))
    senha = db.Column(db.String(12))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "rf_id_code": self.rf_id_code,
            "autorizado": self.autorizado,
            "cpf": self.cpf,
            "tipo": self.tipo.name,
            "senha": self.senha,
        }
