from datos_de_barrio import datos_de_barrio

def obtener_datos_recreacion():
    return [
        datos_de_barrio(
            "recreacion", "Parque y Zona Verde",
            "Parque Vecinal La Coruña",
            "Espacio público de encuentro, descanso y convivencia comunitaria dentro del sector de La Coruña.",
            "Parque Vecinal La Coruña, Ciudad Bolívar",
            "Cartografía y referencia geográfica local", "", 4.5785, -74.1524
        ),
        datos_de_barrio(
            "recreacion", "Cancha Deportiva",
            "Cancha Pública La Coruña",
            "Escenario deportivo abierto para la actividad física, integración vecinal y recreación de los habitantes.",
            "Calle 58C Sur, Barrio La Coruña",
            "Registros comunitarios y cartografía local", "", 4.5789, -74.1518
        ),
    ]