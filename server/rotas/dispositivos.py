from fastapi import APIRouter
from fastapi import status

from base_de_dados import session
from schemas import DeviceSchema
from serviços import ServiçoDispositivo

router = APIRouter(prefix='/dispositivo', tags=['dispositivo'])

@router.get("/", status_code=status.HTTP_200_OK)
async def listar_dispositivos():
    with session:
        lista_dispositivos = ServiçoDispositivo.listar(session)
    return lista_dispositivos

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_dispositivo(device: DeviceSchema):
    with session:
        ServiçoDispositivo.adicionar(device.nome, session)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remover_dispositivo(device: DeviceSchema):
    with session:
        ServiçoDispositivo.remover(device.nome, session)