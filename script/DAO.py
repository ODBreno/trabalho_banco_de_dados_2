from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAO():
    # Conexão com o banco
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/trabalho_bd2")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # Função de inserção no banco
    def insert(session, obj):
        session.add(obj)

# Funções para buscar um registro do banco
class DAODeputados():
    
    def select(session, id):
        dep = session.query(Deputados).filter(Deputados.id == id).first()
        return dep

class DAODespesas():
    
    def select(session, id):
        dep = session.query(Despesas).filter(Despesas.id == id).first()
        return dep

class DAOOrgaos():
    
    def select(session, id):
        dep = session.query(Orgaos).filter(Orgaos.id == id).first()
        return dep

class DAOEventos():

    def select(session, id):
        event = session.query(Evento).filter(Evento.id == id).first()
        return event

class DAOLegislatura():

    def select(session, id):
        legislatura = session.query(Legislatura).filter(Legislatura.id == id).first()
        return legislatura


