SQL_CREATE_COMBUSTIVEL = '''
CREATE TABLE IF NOT EXISTS combustivel(
"id_combustivel"  INTEGER,
"descricao"       TEXT     NOT NULL,
PRIMARY KEY ("id_combustivel" AUTOINCREMENT)
)
'''

SQL_INSERT_COMBUSTIVEL = '''
INSERT INTO combustivel (descricao)
VALUES(?)
'''
SQL_UPDATE_COMBUSTIVEL = '''
UPDATE combustivel
   SET descricao=?
 WHERE id_combustivel=?
'''

SQL_OBTER_TODOS_COMBUSTIVEIS = '''
SELECT id_combustivel, descricao
  FROM combustivel
'''
