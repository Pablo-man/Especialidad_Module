from utils.db import db

class Especialidad(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100))

    def __init__(self, nombre):
        self.nombre= nombre
