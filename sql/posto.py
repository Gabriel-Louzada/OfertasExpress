SQL_CREATE_POSTO = '''
CREATE TABLE IF NOT EXISTS posto(
"id_posto"        INTEGER,
"combustivel"     INTEGER NOT NULL,
"nome_posto"      TEXT    NOT NULL,
"endereco_posto"  TEXT    NOT NULL,
"bairro"          TEXT,
FOREGN KEY ("combustivel") REFERENCES "combustivel_posto("id_combustivel")"
PRIMARY KEY ("id_posto" AUTOINCREMENT)
)
'''

SQL_INSERT_POSTO = '''
INSERT INTO posto(combustivel, nome_posto, endereco_posto, bairro)
VALUES (?,?,?,?)
'''

SQL_UPDATE_POSTO = '''
UPDATE posto
   SET combustivel=?, nome_posto=?, endereco_posto=?, bairro=?
 WHERE id_posto=?
'''

SQL_OBTER_TODOS_POSTOS = '''
SELECT id_posto, combustivel, nome_posto, endereco_posto, bairro
  FROM posto
'''

SQL_OBTER_UM_POSTO = '''
SELECT id_posto, combustivel, nome_posto, endereco_posto, bairro
  FROM posto
 WHERE id_posto=?
'''