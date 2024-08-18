import sqlite3
from models.posto_repo import Posto
from sql.posto import *
from util.conexao import criar_conexao, executar


def criar_tabela_posto():
    try:
        executar(SQL_CREATE_POSTO)
    except sqlite3.Error as e:
        print(f"Erro na função criar_tabela_posto {e}")

def obter_todos_postos() -> list[Posto]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_POSTOS).fetchall()
            return [Posto(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Erro na função obter_todos_postos {e}")
        return None

def inserir_posto(posto: Posto):
    try:
        executar(SQL_INSERT_POSTO,(
            posto.nome_posto,
            posto.endereco_posto,
            posto.bairro
        ))
    except sqlite3.Error as e:
        print(f"Erro na função inserir posto {e}")

def alterar_posto(posto: Posto):
    try:
        executar(SQL_UPDATE_POSTO,(
           posto.nome_posto,
           posto.endereco_posto,
           posto.bairro,
           posto.id_posto
        ))
    except sqlite3.Error as e:
        print(f"Erro na função alterar_posto {e}")

def remover_posto(codigo:int):
    try:
        executar(SQL_REMOVER_POSTO,(codigo,))
    except sqlite3.Error as e:
        print(f"Erro na função remover_posto {e}")