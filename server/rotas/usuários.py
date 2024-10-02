from fastapi import APIRouter
from fastapi import status

from base_de_dados import session
from schemas import UserSchema
from serviços import ServiçoUsuário

router = APIRouter(prefix='/usuário', tags=['usuário'])

@router.get("/", status_code=status.HTTP_200_OK)
async def listar_usuários():
    with session:
        lista_usuários = ServiçoUsuário.listar(session)
    return lista_usuários

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_usuário(user: UserSchema):
    with session:
        ServiçoUsuário.adicionar(user.nome, session)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remover_usuário(user: UserSchema):
    with session:
        ServiçoUsuário.remover(user.nome, session)