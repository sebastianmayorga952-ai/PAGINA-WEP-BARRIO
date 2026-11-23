from flask import Flask, render_template, request, redirect, url_for
from db import db
from datos_de_barrio import datos_de_barrio
from datos import obtener_todos_los_registros

class paginaWEP:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///based_de_datos_barrio.sqlite3"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscarDatos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=['GET', 'POST'])
        self.app.add_url_rule('/poligono', view_func=self.verPoligono)
        self.app.add_url_rule('/vias-acceso', view_func=self.verViasAcceso)

        with self.app.app_context():
            db.create_all()
            if datos_de_barrio.query.count() == 0:
                db.session.add_all(obtener_todos_los_registros())
                db.session.commit()

        self.app.run(debug=True)

    def buscarDatos(self):
        todos_los_datos = datos_de_barrio.query.all()
        return render_template('mostrardatos.html', datos=todos_los_datos)

    def agregar(self):
        if request.method == 'POST':
            mi_dato = datos_de_barrio(
                request.form['categoria'],
                request.form['subcategoria'],
                request.form['nombre'],
                request.form['descripcion'],
                request.form['ubicacion'],
                request.form['fuente_o_dato'],
                request.form['imagen_url'],
                float(request.form.get('latitud') or 4.578193),
                float(request.form.get('longitud') or -74.152101)
            )
            db.session.add(mi_dato)
            db.session.commit()
            return redirect(url_for('buscarDatos'))

        return render_template('CONTENIDO_PAGINA.html')

    def verPoligono(self):
        return render_template('mapa_poligono.html')

    def verViasAcceso(self):
        registros_movilidad = datos_de_barrio.query.filter_by(categoria='movilidad').all()
        vias = [r for r in registros_movilidad if 'Paradero' not in r.subcategoria]
        return render_template('mapa_vias.html', vias_principales=vias)

mi_pagina = paginaWEP()