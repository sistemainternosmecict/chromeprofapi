from fastapi import FastAPI
from src.routes.dispositivo_routes import router

app = FastAPI(title="Gestão de Chromebooks")

app.include_router(router)
