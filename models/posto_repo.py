from dataclasses import dataclass
from typing import Optional

@dataclass
class Posto():
    id_posto: Optional[int] = None
    nome_posto: Optional[str] = None
    endereco_posto: Optional[str] = None
    bairro: Optional[str] = None