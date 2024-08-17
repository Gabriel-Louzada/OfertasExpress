SQL_CREATE_COMBUSTIVEL_POSTO = '''
CREATE TABLE IF NOT EXISTS combustivel_posto(
"id_combustivel"   INTEGER,
"id_posto"         INTEGER       NOT NULL,
"valor"            NUMERIC(8,2)  NOT NULL,
"data_ajuste"      DATE          NOT NULL,
FOREIGN KEY ("id_combustivel") REFERENCES "combustivel"("id_combustivel"),
FOREIGN KEY ("id_posto") REFERENCES "posto"("id_posto"),
PRIMARY KEY ("id_combustivel","id_posto")
)
'''