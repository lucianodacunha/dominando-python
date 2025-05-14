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


class Livro:
    serial: int = 0

    def __init__(
        self, titulo: str, resumo: str, ano: str, paginas: int, isbn: str
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
    def ano(self) -> str:
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


class Categoria:
    serial: int = 0

    def __init__(self, nome: str):
        self._id = Categoria.get_id()
        self._nome = nome

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> None:
        return self._nome

    @classmethod
    def get_id(cls) -> int:
        Categoria.serial += 1
        return Categoria.serial

    def __str__(self) -> str:
        return f"Categoria: {self.nome}"


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
