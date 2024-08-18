SQL_CREATE_POSTO = '''
CREATE TABLE IF NOT EXISTS posto(
"id_posto"        INTEGER,
"nome_posto"      TEXT    NOT NULL,
"endereco_posto"  TEXT    NOT NULL,
"bairro"          TEXT,
PRIMARY KEY ("id_posto" AUTOINCREMENT)
)
'''

SQL_INSERT_POSTO = '''
INSERT INTO posto(nome_posto, endereco_posto, bairro)
VALUES (?,?,?)
'''

SQL_UPDATE_POSTO = '''
UPDATE posto
   SET nome_posto=?, endereco_posto=?, bairro=?
 WHERE id_posto=?
'''

SQL_OBTER_TODOS_POSTOS = '''
SELECT id_posto, nome_posto, endereco_posto, bairro
  FROM posto
'''

SQL_OBTER_UM_POSTO = '''
SELECT id_posto, nome_posto, endereco_posto, bairro
  FROM posto
 WHERE id_posto=?
'''

SQL_REMOVER_POSTO = '''
DELTE FROM posto
WHERE id_posto=?
'''