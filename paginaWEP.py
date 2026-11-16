

from flask import Flask, render_template, request, redirect, url_for
from db import db
from datos_de_barrio import datos_de_barrio

class paginaWEP:
    def __init__(self):


        self.app= Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///based_de_datos_barrio.sqlite3"
        # agregar la db a nuestra aplicacion
        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscarDatos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=['GET', 'POST'])



        #inicio de servidor 
        with self.app.app_context():
            db.create_all()

        self.app.run(debug=True)
    
    def buscarDatos(self):

        return render_template('CONTENIDO_PAGINA.html', datos=datos_de_barrio.query.all())
    
    def agregar(self):
        #procear los datos del formulario y guardarlos en la base de datos
        if request.method=='POST':
            #crear un objeto de la clase datos_de_barrio con los datos del formulario
            nombre=request.form['nombre']
            email=request.form['email']
            codigo=request.form['codigo']

            mi_dato=datos_de_barrio(nombre, email, codigo)

            #gauardar el objeto en la base de datos
            db.session.add(mi_dato)
            db.session.commit()

            return redirect(url_for('buscarDatos'))

            #crear un objeto de la clase datos_de_barrio
            nuevo_dato=datos_de_barrio(nombre, email, codigo)

            #agregar el objeto a la base de datos
            db.session.add(nuevo_dato)
            db.session.commit()
        return render_template('CONTENIDO_PAGINA.html')



mi_pagina=paginaWEP()