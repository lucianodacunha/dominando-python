from model.model_categoria import Categoria
from exception.exceptions import RegistroNaoEncontradoException


class CategoriaDAO:
    def __init__(self) -> None:
        self.__categorias: dict[int, Categoria] = dict()
        self.__sequence = 1

    def inserir(self, categoria: Categoria) -> None:
        categoria.id = self.__sequence
        self.__categorias[categoria.id] = categoria
        self.__sequence += 1

    def listar(self) -> list[Categoria]:
        if not self.__categorias:
            raise RegistroNaoEncontradoException("Nenhum registro encontrado")
        return self.__categorias.values()

    def atualizar(self, id: int, nome: str) -> Categoria:
        categoria = self.buscar_por_id(id)
        categoria.nome = nome
        return categoria

    def excluir(self, id: int) -> Categoria:
        if not self.__categorias.get(id, 0):
            raise RegistroNaoEncontradoException("Registro não encontrado")
        return self.__categorias.pop(id)

    def buscar_por_id(self, id: int) -> Categoria:
        if not self.__categorias.get(id, 0):
            raise RegistroNaoEncontradoException("Registro não encontrado")
        return self.__categorias.get(id)
