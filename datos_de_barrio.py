from db import db

class datos_de_barrio(db.Model):
    # Nombre de la tabla
    __tablename__ = "datos_de_barrio"

    # Llave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Atributos generales del lugar o registro
    categoria = db.Column(db.String(50))       # recreacion, gastronomia, movilidad, seguridad, referencia, historia
    subcategoria = db.Column(db.String(80))    # Ej: Parque, Restaurante, Vía principal, Reporte comunitario...
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    ubicacion = db.Column(db.String(150))
    fuente_o_dato = db.Column(db.String(120))
    imagen_url = db.Column(db.String(250))
    latitud = db.Column(db.Float)              # Coordenada real Latitud (ej: 4.6097)
    longitud = db.Column(db.Float)             # Coordenada real Longitud (ej: -74.0817)

    def __init__(self, categoria, subcategoria, nombre, descripcion, ubicacion, fuente_o_dato="Dato demostrativo", imagen_url="", latitud=4.6097, longitud=-74.0817):
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.fuente_o_dato = fuente_o_dato
        self.imagen_url = imagen_url
        self.latitud = latitud
        self.longitud = longitud