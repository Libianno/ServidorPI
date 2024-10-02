import pytest

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient

from server.modelos import Acesso
from server.modelos import Base
from server.modelos import Cartão
from server.modelos import Dispositivo
from server.modelos import Usuário
from server.entrypoint_fastapi import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)

@pytest.fixture
def usuário(session):
    novo_usuário = Usuário(nome='usuário 1')
    session.add(novo_usuário)
    session.commit()
    return session.scalar(select(Usuário).where(Usuário.nome == 'usuário 1'))

@pytest.fixture
def cartão(session):
    novo_cartão = Cartão(uid=1, id_usuário=1)
    session.add(novo_cartão)
    session.commit()
    return session.scalar(select(Cartão).where(Cartão.uid == 1))

@pytest.fixture
def dispositivo(session):
    novo_dispositivo = Dispositivo(nome='Dispositivo 1')
    session.add(novo_dispositivo)
    session.commit()

    return session.scalar(select(Dispositivo).where(Dispositivo.nome == 'Dispositivo 1'))

@pytest.fixture
def acesso(session):
    novo_acesso = Acesso(id_cartão=1, id_dispositivo=1)
    session.add(novo_acesso)
    session.commit()

    return session.scalar(select(Acesso).where(Acesso.id_cartão == 1))