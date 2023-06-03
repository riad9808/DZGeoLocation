import json

locations = [
    
    {
        "latitude": 31.7426878,
        "longitude" : 6.0472499,
        "name": "Anadarko siege",
        "population": 320
    },
    {
        "latitude": 31.7426878,
        "longitude" : 6.0472499,
        "name": "Ourhoud siege",
        "population": 220
    }
  
   
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