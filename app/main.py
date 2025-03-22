from fastapi import FastAPI
from .routes import clients, payments, auth

app = FastAPI(title="Газ Контроль API")

app.include_router(clients.router)
app.include_router(payments.router)
app.include_router(auth.router)