from fastapi import FastAPI
from .routes import clients, payments, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Газ Контроль API")

@app.get("/")
def read_root():
    return {"message": "Сервер работает!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены (["http://localhost:3000"] для фронта)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon"}

app.include_router(clients.router)
app.include_router(payments.router)
app.include_router(auth.router)