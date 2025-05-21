from model.model_autor import Autor
from exception.exceptions import RegistroNaoEncontradoException


class Autor_DAO:
    def __init__(self) -> None:
        self.__autores: dict[int, Autor] = dict()
        self.__sequence: int = 1

    def listar(self) -> dict[int, Autor]:
        if not self.__autores:
            raise RegistroNaoEncontradoException("Nenhum autor cadastrado")
        return self.__autores.values()

    def cadastrar(self, autor: Autor) -> None:
        autor.id = self.__sequence
        self.__autores[autor.id] = autor
        self.__sequence += 1

    def excluir(self, id: int) -> Autor:
        if self.__autores.get(id, 0):
            return self.__autores.pop(id, 0)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")

    def listar_por_id(self, id: int) -> Autor:
        if self.__autores.get(id, 0):
            return self.__autores.get(id)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")

    def editar(self, id: int, nome: str, bio: str) -> Autor:
        autor = self.listar_por_id(id)
        autor.nome = nome
        autor.biografia = bio
        return autor
