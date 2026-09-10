import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

# Приветствие сервис берёт из окружения.
# Нет переменной GREETING — сервис не стартует.
greeting = os.environ["GREETING"]


@app.get("/")
def read_root():
    return {"message": greeting}


@app.get("/health")
def health_check():
    return {"status": "ok"}
