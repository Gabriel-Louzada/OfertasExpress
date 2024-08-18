import sqlite3
from models.combustivel_posto_models import Combustivel_posto
from sql.combustivel_posto import *
from util.conexao import executar, criar_conexao

def criar_tabela_combustivel_posto():
    try:
        executar(SQL_CREATE_COMBUSTIVEL_POSTO)
    except sqlite3.Error as e:
        print(f"Erro na função criar_tabela_combustivel_posto {e}")

def obter_todos_combustivel_posto() -> list[Combustivel_posto]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_COMBUSTIVEL_POSTO).fetchall()
            return [Combustivel_posto(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Errp ma Função obter_todos_combustivel_posto {e}")

def inserir_combustivel_posto(combustivel_posto: Combustivel_posto):
    try:
        executar(SQL_INSERT_COMBUSTIVEL_POSTO,(
            combustivel_posto.id_combustivel,
            combustivel_posto.id_posto,
            combustivel_posto.valor,
            combustivel_posto.data_ajuste
        ))
    except sqlite3.Error as e:
        print(f"Erro na função inserir_combustivel_posto {e}")

def alterar_combustivel_posto(combustivel_posto: Combustivel_posto):
    try:
        executar(SQL_UPDATE_COMBUSTIVEL_POSTO,(
            combustivel_posto.id_combustivel,
            combustivel_posto.id_posto,
            combustivel_posto.valor,
            combustivel_posto.data_ajuste,
            combustivel_posto.id_combustivel_posto
        ))
    except sqlite3.Error as e:
        print(f"Erro na função inserir_combustivel_posto {e}")        