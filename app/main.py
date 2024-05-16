from fastapi import FastAPI

import json
# Créer une instance de l'application FastAPI

app = FastAPI()
with open("data/meteo.json", "r") as json_file:
    data= json.load(json_file)
# Définir une route
@app.get("/")
def read_root():
    return data