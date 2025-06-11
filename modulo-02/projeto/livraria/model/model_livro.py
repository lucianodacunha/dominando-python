class Livro:
    __slot__ = ("__titulo", "__resumo", "__ano", "__paginas", "__isbn")

    def __init__(
        self, titulo: str, resumo: str, ano: int, paginas: int, isbn: str
    ) -> None:
        self.__titulo = titulo
        self.__resumo = resumo
        self.__ano = ano
        self.__paginas = paginas
        self.__isbn = isbn

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str) -> None:
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> str:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int) -> None:
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        self.__isbn = isbn

    def __str__(self) -> str:
        return f"{str(id).zfill(2)} - {self.titulo}"
