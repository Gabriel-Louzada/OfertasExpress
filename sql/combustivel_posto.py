SQL_CREATE_COMBUSTIVEL_POSTO = '''
CREATE TABLE IF NOT EXISTS combustivel_posto(
"id_combustivel_posto"   INTEGER,
"id_combustivel"         INTEGER,
"id_posto"               INTEGER       NOT NULL,
"valor"                  NUMERIC(8,2)  NOT NULL,
"data_ajuste"            DATE          NOT NULL,
FOREIGN KEY ("id_combustivel") REFERENCES "combustivel"("id_combustivel"),
FOREIGN KEY ("id_posto") REFERENCES "posto"("id_posto"),
PRIMARY KEY ("id_combustivel","id_posto")
PRIMARY KEY ("id_combustivel_posto" AUTOINCREMENT)
)
'''

SQL_INSERT_COMBUSTIVEL_POSTO = '''
INSERT INTO combustivel_posto(id_combustivel, id_posto, valor, data_ajuste)
VALUES (?,?,?,?)
'''

SQL_UPDATE_COMBUSTIVEL_POSTO = '''
UPDATE combustivel_posto
   SET  valor=?, data_ajuste=?
 WHERE id_combustivel=?, id_posto=?
'''

SQL_OBTER_TODOS_COMBUSTIVEL_POSTO =  '''
SELECT id_combustivel, id_posto, valor, data_ajuste
  FROM combustivel_posto
'''

SQL_OBTER_UM_COMBUSTIVEL_POSTO = '''
SELECT id_combustivel, id_posto, valor, data_ajuste
  FROM combustivel_posto
 WHERE id_combustivel=?, id_posto=?,
'''

#ATÉ O PRESENTE MOMENTO NAO VEJO A NECESSIDADE DE CRIAR UMA FUNÇÃO DELETE PARA ESSA TABELA COMBUSTIVEL_POSTO