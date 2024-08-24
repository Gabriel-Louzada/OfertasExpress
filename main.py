from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from repo.combustivel_posto_repo import criar_tabela_combustivel_posto
from repo.combustivel_repo import criar_tabela_combustivel
from repo.posto_repo import criar_tabela_posto
from routes import combustivel_router, main_router
from routes import combustivel_router


criar_tabela_posto()
criar_tabela_combustivel()
criar_tabela_combustivel_posto()

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(main_router.router)
app.include_router(combustivel_router.router)

print("Tudo certo no MAIN")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8001)