import json

locations = [
    {
        "latitude": 31.688480,
        "longitude" : 6.065760,
        "name": "Anadarko siege",
        "population": 320
    },
  
   
]

features = []
for location in locations:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [location["longitude"], location["latitude"]]
        },
        "properties": {
            "name": location["name"],
            "population": location["population"]
        }
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

with open("data.geojson", "w") as f:
    json.dump(geojson_data, f)