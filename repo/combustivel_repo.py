import sqlite3
from models.combustivel_models import Combustivel
from sql.combustivel import *
from util.conexao import criar_conexao, executar


def criar_tabela_combustivel():
    try:
        executar(SQL_CREATE_COMBUSTIVEL)
    except sqlite3.Error as e:
        print(f"Erro na função criar_tabela {e}")
    

def obter_todos_combustiveis() -> list[Combustivel]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_COMBUSTIVEIS).fetchall()
            return [Combustivel(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Erro ao na função obter_todos_combustiveis {e}")
        return None

def inserir_combustivel(combustivel: Combustivel):
    try:
        executar(SQL_INSERT_COMBUSTIVEL,(
            combustivel.descricao,
        ))
    except:
        print(f"Erro na função inserir_combustivel")

def alterar_combustivel(combustivel: Combustivel):
    try:
        executar(SQL_UPDATE_COMBUSTIVEL,(
            combustivel.descricao,
            combustivel.id_combustivel
            ))
    except:
        print(f"Erro na função alterar_combustivel")

#ATÉ O PRESENTE MOMENTO NAO VEJO NECESSIDADE DE REMOVER UM COMBUSTIVEL 