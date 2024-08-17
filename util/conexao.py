import sqlite3

def criar_conexao():
    conexao = sqlite3.connect("DataBase.db")
    return conexao

def executar(comando):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(comando)
    except sqlite3.Error as e:
        print(f"Erro ao executar o {comando}")