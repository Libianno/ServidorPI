from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Usuário(Base):
    """
    Classe que modela a tabela de usuário no banco de dados
    """
    __tablename__ = 'usuários'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]


class Cartão(Base):
    __tablename__ = 'cartões'

    uid: Mapped[int] = mapped_column(primary_key=True)
    id_usuário: Mapped[int] = mapped_column(ForeignKey("usuários.id"))


class Dispositivo(Base):
    __tablename__ = 'dispositivos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]


class Acesso(Base):
    __tablename__ = 'acessos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    data: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    id_cartão: Mapped[int] = mapped_column(ForeignKey("cartões.uid"))
    id_dispositivo: Mapped[int] = mapped_column(ForeignKey("dispositivos.id"))