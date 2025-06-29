from fastapi import FastAPI

app = FastAPI()
clientes = []

@app.post("/clientes/")
def agregar_cliente(nombre: str):
    clientes.append({"nombre": nombre})
    return {"mensaje": f"Cliente {nombre} agregado"}

@app.get("/clientes/")
def listar_clientes():
    return {"clientes": clientes}
