from db import db

class datos_de_barrio(db.Model):

        #nombre de tabla 

        __tablename__="datos_de_barrio"

        #conjunto de atributos que van a ser los campos de la tabla 

        #LLAVE PRIMARIA

        id=db.Column(db.Integer, primary_key=True)

        NOMBRE=db.Column(db.String(50))
        EMAIL=db.Column(db.String(100))
        CODIGO=db.Column(db.String(10))

        # metodo constructor que va a recibir los datos de la tabla y los va a guardar en los atributos de la clases

        def __init__(self, NOMBRE, EMAIL, CODIGO):
                self.NOMBRE=NOMBRE
                self.EMAIL=EMAIL
                self.CODIGO=CODIGO  