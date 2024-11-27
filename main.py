from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

# Ruta principal para verificar la conexión
@app.get("/")
def read_root():
    return {"message": "La API está funcionando"}
