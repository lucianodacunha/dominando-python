class Livro:
    serial: int = 0

    def __init__(
        self, titulo: str, resumo: str, ano: int, paginas: int, isbn: str
    ) -> None:
        self._id = Livro.get_id()
        self._titulo = titulo
        self._resumo = resumo
        self._ano = ano
        self._paginas = paginas
        self._isbn = isbn

    @property
    def id(self) -> int:
        return self._id

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo

    @property
    def resumo(self) -> str:
        return self._resumo

    @property
    def ano(self) -> int:
        return self._ano

    @property
    def paginas(self) -> str:
        return self._paginas

    @property
    def isbn(self) -> str:
        return self._isbn

    @resumo.setter
    def resumo(self, resumo: str) -> None:
        self._resumo = resumo

    @classmethod
    def get_id(cls):
        Livro.serial += 1
        return Livro.serial

    def __str__(self) -> str:
        return f"{str(id).zfill(2)} - {self.titulo}"
