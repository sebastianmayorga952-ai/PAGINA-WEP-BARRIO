from flask import Flask, render_template, request, redirect, url_for
from db import db
from datos_de_barrio import datos_de_barrio

class paginaWEP:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///based_de_datos_barrio.sqlite3"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Agregar la db a nuestra aplicacion
        db.init_app(self.app)

        # Registro de rutas usando add_url_rule
        self.app.add_url_rule('/', view_func=self.buscarDatos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=['GET', 'POST'])

        # Inicio de servidor y creacion de tablas
        with self.app.app_context():
            db.create_all()
            self.cargarDatosDemostrativos()

        self.app.run(debug=True)

    def cargarDatosDemostrativos(self):
        if datos_de_barrio.query.count() == 0:
            ejemplos = [
                # B. Recreacion
                datos_de_barrio(
                    "recreacion", "Parque y Zona Verde",
                    "Parque Central del Sector (Demostrativo)",
                    "Espacio arborizado con senderos peatonales, juegos infantiles y zona de descanso familiar.",
                    "Calle 10 # 15 - 20 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6105, -74.0825
                ),
                datos_de_barrio(
                    "recreacion", "Cancha Deportiva y Coliseo",
                    "Polideportivo Comunitario Norte (Demostrativo)",
                    "Cancha múltiple para microfútbol y baloncesto junto a gimnasio al aire libre.",
                    "Carrera 14 # 12 - 05 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6118, -74.0805
                ),
                # C. Comidas y Comercio
                datos_de_barrio(
                    "gastronomia", "Cafetería y Panadería",
                    "Panadería Tradicional La Esquina (Demostrativo)",
                    "Pan artesanal horneado en la mañana, cafetería tradicional y punto habitual de desayuno.",
                    "Carrera 15 # 10 - 02 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6095, -74.0818
                ),
                datos_de_barrio(
                    "gastronomia", "Restaurante y Puestos Callejeros",
                    "Plazoleta Gastronómica del Barrio (Demostrativo)",
                    "Corredor con restaurantes de comida típica, comidas rápidas y puestos nocturnos.",
                    "Avenida Principal con Calle 9 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6088, -74.0810
                ),
                datos_de_barrio(
                    "gastronomia", "Establecimiento Comercial",
                    "Autoservicio y Miscelánea El Vecino (Demostrativo)",
                    "Abastecimiento de víveres, papelería escolar y productos de primera necesidad.",
                    "Calle 8 # 16 - 30 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6082, -74.0830
                ),
                # D. Tipo de orden - Movilidad
                datos_de_barrio(
                    "movilidad", "Camino Principal y Transporte",
                    "Avenida Principal del Sector (Demostrativo)",
                    "Eje vial principal con circulación de transporte público, paraderos y ciclorruta.",
                    "Corredor Vial Principal (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6097, -74.0802
                ),
                datos_de_barrio(
                    "movilidad", "Conjuntos y Casa Común",
                    "Salón Comunal y Sector Residencial (Demostrativo)",
                    "Casa común de reuniones vecinales y zona de conjuntos residenciales organizados.",
                    "Calle 10 # 13 - 15 (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6102, -74.0815
                ),
                # E. Tipo de orden - Seguridad
                datos_de_barrio(
                    "seguridad", "Precaución Nocturna (Reporte Comunitario)",
                    "Tramo Peatonal Poco Iluminado (Demostrativo)",
                    "Sector reportado por vecinos con baja iluminación en horario nocturno. Se recomienda precaución.",
                    "Calle 13 con Carrera 17 (Ubicación demostrativa)",
                    "Reporte comunitario no oficial (Demostrativo)", "", 4.6122, -74.0835
                ),
                # F y G. Turistica (Referencia e Historia)
                datos_de_barrio(
                    "referencia", "Punto de Referencia e Institución",
                    "Parroquia y Colegio Principal del Barrio (Demostrativo)",
                    "Punto tradicional de encuentro comunitario y referencia clave para orientarse en el barrio.",
                    "Frente al Parque Central (Ubicación demostrativa)",
                    "Dato demostrativo", "", 4.6107, -74.0820
                ),
                datos_de_barrio(
                    "historia", "Origen y Evolución del Barrio",
                    "Sector Fundacional del Barrio (Demostrativo)",
                    "Relato demostrativo: Primeras manzanas trazadas por las familias fundadoras y consolidación comercial.",
                    "Sector Histórico Central (Ubicación demostrativa)",
                    "Memoria barrial / Dato demostrativo", "", 4.6099, -74.0822
                )
            ]
            db.session.add_all(ejemplos)
            db.session.commit()

    def buscarDatos(self):
        todos_los_datos = datos_de_barrio.query.all()
        return render_template('mostrardatos.html', datos=todos_los_datos)

    def agregar(self):
        if request.method == 'POST':
            categoria = request.form['categoria']
            subcategoria = request.form['subcategoria']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            ubicacion = request.form['ubicacion']
            fuente_o_dato = request.form['fuente_o_dato']
            imagen_url = request.form['imagen_url']
            latitud = float(request.form.get('latitud') or 4.6097)
            longitud = float(request.form.get('longitud') or -74.0817)

            mi_dato = datos_de_barrio(
                categoria, subcategoria, nombre, descripcion,
                ubicacion, fuente_o_dato, imagen_url, latitud, longitud
            )

            db.session.add(mi_dato)
            db.session.commit()

            return redirect(url_for('buscarDatos'))

        return render_template('CONTENIDO_PAGINA.html')


mi_pagina = paginaWEP()