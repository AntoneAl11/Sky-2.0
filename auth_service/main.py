from fastapi import FastAPI

app = FastAPI()
usuarios = {"admin": "1234"}

@app.post("/login/")
def login(usuario: str, contrasena: str):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        return {"status": "Acceso concedido"}
    return {"status": "Acceso denegado"}

