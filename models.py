from main import db

# models
class Usuario(db.Model):
    id = db.Column(db.String(9), primary_key= True)
    name = db.Column(db.String(50))
    rfid_id_code = db.Column(db.String(11))
    autorizado = db.Column(db.Boolean())

    def to_json(self):
        return {"id": self.id, "name": self.name, "rfid_id_code": self.rfid_id_code, "autorizado": self.autorizado}
