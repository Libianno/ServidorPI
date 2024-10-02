from fastapi import FastAPI

from rotas import usuários, cartões, dispositivos, acessos

app = FastAPI()

app.include_router(usuários.router)
app.include_router(cartões.router)
app.include_router(dispositivos.router)
app.include_router(acessos.router)
