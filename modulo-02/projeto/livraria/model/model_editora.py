class Editora:
    __slots__ = ("__id", "__nome", "__endereco", "__telefone")

    def __init__(self, nome: str, endereco: str, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

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
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        self.__endereco = endereco

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self.__telefone = telefone

    def __str__(self) -> str:
        return f"Editora: {self.nome}"
