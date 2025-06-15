from dataclasses import dataclass

@dataclass
class Categoria:
    id: int = 0
    nome: str = ""

    @classmethod
    def from_row(cls, row: tuple):
        return cls(
            id=row[0],
            nome=row[1]
        )
