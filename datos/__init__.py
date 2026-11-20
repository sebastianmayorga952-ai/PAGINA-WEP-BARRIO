from .recreacion import obtener_datos_recreacion
from .comidas_comercio import obtener_datos_comercio
from .educacion_referentes import obtener_datos_educacion
from .orden_movilidad import obtener_datos_orden

def obtener_todos_los_registros():
    return (
        obtener_datos_recreacion() +
        obtener_datos_comercio() +
        obtener_datos_educacion() +
        obtener_datos_orden()
    )