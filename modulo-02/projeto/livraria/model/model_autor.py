class Autor:
    __slots__ = ("__id", "__nome", "__biografia")

    def __init__(self, nome: str, biografia: str) -> None:
        self.nome = nome
        self.biografia = biografia

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        """Método setter da propriedade id"""
        self.__id = id

    @property
    def nome(self) -> str:
        """Método getter da propriedade nome"""
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def biografia(self) -> str:
        return self.__biografia

    @biografia.setter
    def biografia(self, biografia: str) -> None:
        self.__biografia = biografia

    def __str__(self) -> str:
        return f"{str(self.id).zfill(2)} - {self.nome}"
