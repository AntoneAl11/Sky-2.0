from fastapi import FastAPI
import json, os

app = FastAPI()
CARPETA = "data"

@app.post("/archivos/{nombre}")
def guardar_archivo(nombre: str, datos: dict):
    ruta = f"{CARPETA}/{nombre}.json"
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo)
    return {"mensaje": f"Archivo de {nombre} guardado"}

@app.get("/archivos/{nombre}")
def leer_archivo(nombre: str):
    ruta = f"{CARPETA}/{nombre}.json"
    if not os.path.exists(ruta):
        return {"error": "Cliente no encontrado"}
    with open(ruta) as archivo:
        datos = json.load(archivo)
    return {"cliente": nombre, "datos": datos}
