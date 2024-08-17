from dataclasses import dataclass
from typing import Optional

@dataclass
class Combustivel():
    id_combustivel = Optional[int] = None
    descricao = Optional[str] = None
    