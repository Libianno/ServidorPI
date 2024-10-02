from sqlalchemy import delete
from sqlalchemy import select

from modelos import Acesso
from modelos import Cartão
from modelos import Dispositivo
from modelos import Usuário

class ServiçoUsuário:
    def adicionar(nome, session):
        novo_usuário = Usuário(nome=nome)
        session.add(novo_usuário)
        session.commit()
    
    def listar(session):
        return session.scalars(select(Usuário)).all()

    def remover(nome, session):
        user = session.scalar(select(Usuário).where(Usuário.nome == nome))
        session.delete(user)
        session.commit()

class  ServiçoCartão:
    def adicionar(nome_usuário, UID, session):
        usuário = session.scalar(select(Usuário).where(Usuário.nome == nome_usuário))

        novo_cartão = Cartão(uid=UID, id_usuário=usuário.id)
        session.add(novo_cartão)
        session.commit()
    
    def listar(session):
        return session.scalars(select(Cartão)).all()

    def remover(UID, session):
        cartão = session.scalar(select(Cartão).where(Cartão.uid == UID))
        session.delete(cartão)
        session.commit()

class  ServiçoDispositivo:
    def adicionar(nome, session):
        novo_dispositivo = Dispositivo(nome=nome)
        session.add(novo_dispositivo)
        session.commit()
    
    def listar(session):
        return session.scalars(select(Dispositivo)).all()

    def remover(nome, session):
        dispositivo = session.scalar(select(Dispositivo).where(Dispositivo.nome == nome))
        session.delete(dispositivo)
        session.commit()

class  ServiçoAcesso:
    def adicionar(UID, id_dispositivo, session):
        novo_dispositivo = Acesso(id_cartão=UID, id_dispositivo=id_dispositivo)
        session.add(novo_dispositivo)
        session.commit()
    
    def listar_formatado(session):
        acessos = list(session.scalars(select(Acesso)).all())
        tabela = []
        for acesso in acessos:
            print(acesso)
            cartão = session.scalar(
                select(Cartão)
                .where(
                    Cartão.uid == acesso.id_cartão
                    ))
            print(cartão)
            usuário = session.scalar(
                select(Usuário).where(
                    Usuário.id == cartão.id_usuário
                ))
            dispositivo = session.scalar(
                select(Dispositivo).where(
                    Dispositivo.id == acesso.id_dispositivo
                ))
            tabela.append(
            {   
                'ID': acesso.id,
                'Data': acesso.data,
                'Cartão': acesso.id_cartão,
                'Usuário': usuário.nome,
                'Dispositivo': dispositivo.nome
            }
            )
        return tabela