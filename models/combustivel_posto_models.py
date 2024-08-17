from dataclasses import dataclass
from typing import Optional

@dataclass
class Combustivel_posto():
    id_combustivel_posto = Optional[int] = None
    id_combustivel = Optional[int] = None
    id_posto = Optional[int] = None
    valor = Optional[str] = None
    data_ajuste = Optional[str] = None