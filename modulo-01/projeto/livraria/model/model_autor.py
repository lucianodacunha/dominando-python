class Autor:
    serial: int = 0

    def __init__(self, nome: str, biografia: str) -> None:
        self._id = Autor.get_id()
        self._nome = nome
        self._biografia = biografia

    @property
    def id(self) -> int:
        return self._id

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

    @classmethod
    def get_id(cls):
        Autor.serial += 1
        return Autor.serial

    def __str__(self) -> str:
        return f"{str(id).zfill(2)} - {self.nome}"
