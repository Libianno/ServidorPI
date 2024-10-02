from fastapi import APIRouter
from fastapi import status

from base_de_dados import session
from schemas import AccessSchema
from serviços import ServiçoAcesso

router = APIRouter(prefix='/acesso', tags=['acesso'])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_acesso(acesso: AccessSchema):
    with session:
        ServiçoAcesso.adicionar(
            acesso.uid, 
            acesso.device_id, 
            session
            )