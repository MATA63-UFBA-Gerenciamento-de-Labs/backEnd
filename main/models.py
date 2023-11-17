from main import db

# models
class Usuario(db.Model):
    id = db.Column(db.String(30), primary_key= True)
    autorizado = db.Column(db.String(1))

    def to_json(self):
        return {"id": self.id, "autorizado": self.autorizado}
