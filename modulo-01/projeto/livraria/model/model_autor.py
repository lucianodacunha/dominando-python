class Autor:
    def __init__(self, nome: str, biografia: str) -> None:
        self._id = 0
        self._nome = nome
        self._biografia = biografia

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id) -> None:
        self._id = id

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def biografia(self) -> str:
        return self._biografia

    @biografia.setter
    def biografia(self, biografia: str) -> None:
        self._biografia = biografia

    def __str__(self) -> str:
        return f"{str(self.id).zfill(2)} - {self.nome}"
