from fastapi import FastAPI
from src.routes.dispositivo_routes import router
from src.models import init_db

app = FastAPI(title="Gestão de Chromebooks")


@app.on_event("startup")
def startup_event():
    init_db()
    print("Banco de dados inicializado com sucesso!")


app.include_router(router)
