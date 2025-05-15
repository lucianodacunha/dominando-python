class Editora:
    serial: int = 0

    def __init__(self, nome: str):
        self._id = Editora.get_id()
        self._nome = nome

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> None:
        return self._nome

    @classmethod
    def get_id(cls) -> int:
        Editora.serial += 1
        return Editora.serial

    def __str__(self) -> str:
        return f"Editora: {self.nome}"
