from model.model_livro import Livro
from exception.exceptions import RegistroNaoEncontradoException


class LivroDAO:

    def __init__(self) -> None:
        self.__livros: dict[int, Livro] = dict()
        self.__sequence: int = 1

    def inserir(self, livro: Livro) -> Livro:
        livro.id = self.__sequence
        self.__livros[livro.id] = livro
        self.__sequence += 1
        return self.__livros[livro.id]

    def listar(self) -> dict[int, Livro]:
        if not self.__livros:
            raise RegistroNaoEncontradoException("Nenhum autor cadastrado")
        return self.__livros.values()

    def atualizar(
        self, id: int, titulo: str, resumo: str, ano: int, paginas: int, isbn: str
    ) -> Livro:
        livro = self.buscar_por_id(id)
        livro.titulo = titulo
        livro.resumo = resumo
        livro.ano = ano
        livro.paginas = paginas
        livro.isbn = isbn
        return livro

    def excluir(self, id: int) -> Livro:
        if self.__livros.get(id, 0):
            return self.__livros.pop(id, 0)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")

    def buscar_por_id(self, id: int) -> Livro:
        if self.__livros.get(id, 0):
            return self.__livros.get(id)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")
