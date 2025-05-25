from model.model_editora import Editora
from exception.exceptions import RegistroNaoEncontradoException


class EditoraDAO:
    def __init__(self):
        self.__editoras: dict[int, Editora] = dict()
        self.__sequence: int = 1

    def inserir(self, editora: Editora) -> Editora:
        editora.id = self.__sequence
        self.__editoras[editora.id] = editora
        self.__sequence += 1
        return self.__editoras[editora.id]

    def listar(self) -> dict[int, Editora]:
        if not self.__editoras:
            raise RegistroNaoEncontradoException("Nenhum autor cadastrado")
        return self.__editoras.values()

    def atualizar(self, id: int, nome: str) -> Editora:
        editora = self.buscar_por_id(id)
        editora.nome = nome
        return editora

    def excluir(self, id: int) -> Editora:
        if self.__editoras.get(id, 0):
            return self.__editoras.pop(id, 0)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")

    def buscar_por_id(self, id: int) -> Editora:
        if self.__editoras.get(id, 0):
            return self.__editoras.get(id)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")
