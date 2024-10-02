from datetime import datetime

from sqlalchemy import select

from server.modelos import Acesso
from server.modelos import Cartão
from server.modelos import Dispositivo
from server.modelos import Usuário


def test_criar_usuário(session):
    novo_usuário = Usuário(nome='usuário 1')
    session.add(novo_usuário)
    session.commit()

    user = session.scalar(select(Usuário).where(Usuário.nome == 'usuário 1'))

    assert user.id == 1
    assert user.nome == 'usuário 1'

def test_criar_cartão(session):
    novo_cartão = Cartão(uid=1, id_usuário=1)
    session.add(novo_cartão)
    session.commit()

    cartão = session.scalar(select(Cartão).where(Cartão.uid == 1))

    assert cartão.uid == 1
    assert cartão.id_usuário == 1

def test_criar_dispositivo(session):
    novo_dispositivo = Dispositivo(nome='Dispositivo 1')
    session.add(novo_dispositivo)
    session.commit()

    dispositivo = session.scalar(select(Dispositivo).where(Dispositivo.nome == 'Dispositivo 1'))

    assert dispositivo.id == 1
    assert dispositivo.nome == 'Dispositivo 1'

def test_criar_acesso(session):
    novo_acesso = Acesso(id_cartão=1, id_dispositivo=1)
    session.add(novo_acesso)
    session.commit()

    acesso = session.scalar(select(Acesso).where(Acesso.id_cartão == 1))

    assert type(acesso.data) == datetime
    assert acesso.id == 1
    assert acesso.id_cartão == 1
    assert acesso.id_dispositivo == 1

def test_cartão_do_usuário(session, usuário, cartão):
    user = session.scalar(select(Usuário).where(Usuário.id == cartão.id_usuário))
    
    assert usuário.nome == user.nome

def test_usuário_do_acesso(session, usuário, cartão, acesso):
    access = session.scalar(select(Acesso).where(Acesso.id_cartão == acesso.id))
    card = session.scalar(select(Cartão).where(Cartão.uid == access.id_cartão))
    user = session.scalar(select(Usuário).where(Usuário.id == card.id_usuário))
    
    assert card.uid == cartão.uid
    assert user.nome == usuário.nome
    