from fastapi import FastAPI

app = FastAPI()
servicios = []

@app.post("/servicios/")
def agregar_servicio(cliente: str, tipo: str, precio: float):
    servicios.append({"cliente": cliente, "tipo": tipo, "precio": precio})
    return {"mensaje": f"Servicio {tipo} agregado al cliente {cliente}"}

@app.get("/servicios/")
def listar_servicios():
    return {"servicios": servicios}
