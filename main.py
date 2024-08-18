from fastapi import FastAPI
from repo.combustivel_posto_repo import criar_tabela_combustivel_posto
from repo.combustivel_repo import criar_tabela_combustivel
from repo.posto_repo import criar_tabela_posto


criar_tabela_posto()
criar_tabela_combustivel()
criar_tabela_combustivel_posto()

app = FastAPI()


print("Tudo certo no MAIN")