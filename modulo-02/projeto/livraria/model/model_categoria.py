class Categoria:
    __slots__ = ("__id", "__nome")

    def __init__(self, nome: str):
        self.nome = nome

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    def __str__(self) -> str:
        return f"Categoria: {self.nome}"
