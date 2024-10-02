from datetime import datetime

import pytest
from sqlalchemy import select
from sqlalchemy.orm.exc import ObjectDeletedError

from server.serviços import ServiçoAcesso
from server.serviços import ServiçoCartão
from server.serviços import ServiçoDispositivo
from server.serviços import ServiçoUsuário
from server.modelos import Acesso
from server.modelos import Cartão
from server.modelos import Dispositivo
from server.modelos import Usuário

def test_adicionar_usuário(session):
    nome = 'usuário 1'
    ServiçoUsuário.adicionar(nome, session)

    user = session.scalar(select(Usuário).where(Usuário.nome == nome))

    assert user.id == 1
    assert user.nome == nome

def test_listar_usuários(usuário, session):
    lista_usuários = ServiçoUsuário.listar(session)

    assert type(lista_usuários) == list
    assert lista_usuários[0].nome == usuário.nome

def test_remover_usuário(usuário, session):
    ServiçoUsuário.remover(usuário.nome, session)
    with pytest.raises(ObjectDeletedError):
        session.scalar(select(Usuário).where(Usuário.nome == usuário.nome))

def test_adicionar_cartão(usuário, session):
    nome = usuário.nome
    UID = 1

    ServiçoCartão.adicionar(nome, UID, session)

    cartão = session.scalar(select(Cartão).where(Cartão.uid == 1))

    assert cartão.uid == 1
    assert cartão.id_usuário == 1

def test_remover_cartão(cartão, session):
    ServiçoCartão.remover(cartão.uid, session)
    with pytest.raises(ObjectDeletedError):
        session.scalar(select(Cartão).where(Cartão.uid == cartão.uid))

def test_adicionar_dispositivo(session):
    nome = 'Dispositivo 1'

    ServiçoDispositivo.adicionar(nome, session)

    dispositivo = session.scalar(select(Dispositivo).where(Dispositivo.nome == 'Dispositivo 1'))

    assert dispositivo.id == 1
    assert dispositivo.nome == 'Dispositivo 1'

def test_remover_dispositivo(dispositivo, session):
    ServiçoDispositivo.remover(dispositivo.nome, session)
    with pytest.raises(ObjectDeletedError):
        session.scalar(select(Dispositivo).where(Dispositivo.nome == dispositivo.nome))

def test_adicionar_acesso(session):
    UID = 1
    id_dispositivo = 1

    ServiçoAcesso.adicionar(UID, id_dispositivo, session)

    acesso = session.scalar(select(Acesso).where(Acesso.id_cartão == 1))

    assert type(acesso.data) == datetime
    assert acesso.id == 1
    assert acesso.id_cartão == 1
    assert acesso.id_dispositivo == 1