import json

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "via_id": "autopista_sur",
                "nombre": "Autopista Sur"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-74.1735, 4.5948],
                    [-74.1678, 4.5945],
                    [-74.1618, 4.5941],
                    [-74.1558, 4.5936],
                    [-74.1495, 4.5930],
                    [-74.1432, 4.5924],
                    [-74.1365, 4.5919],
                    [-74.1300, 4.5914]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "via_id": "av_villavicencio",
                "nombre": "Avenida Ciudad de Villavicencio"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-74.1642, 4.5786],
                    [-74.1605, 4.5778],
                    [-74.1568, 4.5775],
                    [-74.1533, 4.5784],
                    [-74.1498, 4.5766],
                    [-74.1462, 4.5754],
                    [-74.1422, 4.5782],
                    [-74.1380, 4.5815],
                    [-74.1335, 4.5844],
                    [-74.1292, 4.5866]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "via_id": "av_gaitan_cortes",
                "nombre": "Avenida Jorge Gaitán Cortés (Carrera 51)"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-74.1618, 4.5941],
                    [-74.1613, 4.5902],
                    [-74.1604, 4.5865],
                    [-74.1585, 4.5828],
                    [-74.1555, 4.5796],
                    [-74.1533, 4.5784],
                    [-74.1518, 4.5745],
                    [-74.1492, 4.5705],
                    [-74.1455, 4.5675],
                    [-74.1415, 4.5668]
                ]
            }
        }
    ]
}

with open("static/vias_coruna.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

print("¡Listo! Archivo generado en static/vias_coruna.geojson")