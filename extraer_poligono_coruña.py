import json

with open("SECTOR.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filtrar únicamente el código catastral oficial de LA CORUNA (002420)
filtrados = [
    feat for feat in data["features"]
    if feat.get("properties", {}).get("SCACODIGO") == "002420"
]

resultado = {"type": "FeatureCollection", "features": filtrados}

with open("static/la_coruna.geojson", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False)

print(f"Total polígonos guardados: {len(filtrados)}")