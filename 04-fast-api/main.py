from fastapi import FastAPI

app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def message():
    return "Hello there! Im learning FastAPI"