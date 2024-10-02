from fastapi import APIRouter
from fastapi import status

from base_de_dados import session
from schemas import CardSchema, UserSchema
from serviços import ServiçoCartão

router = APIRouter(prefix='/cartão', tags=['cartão'])

@router.get("/", status_code=status.HTTP_200_OK)
async def listar_cartões():
    with session:
        lista_cartões = ServiçoCartão.listar(session)
    return lista_cartões

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_cartão(user: UserSchema, card: CardSchema):
    with session:
        ServiçoCartão.adicionar(user.nome, card.uid, session)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remover_usuário(card: CardSchema):
    with session:
        ServiçoCartão.remover(card.uid, session)