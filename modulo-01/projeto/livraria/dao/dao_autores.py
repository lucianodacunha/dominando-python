from model.model_autor import Autor
from exception.exceptions import RegistroNaoEncontradoException

autores: dict[int, Autor] = dict()


def listar() -> dict[int, Autor]:
    if not autores:
        raise RegistroNaoEncontradoException("Nenhum autor cadastrado")
    return autores


def excluir(id: int) -> Autor:
    if autores.get(id, 0):
        return autores.pop(id, 0)
    else:
        raise RegistroNaoEncontradoException("Registro não encontrado")


def listar_por_id(id: int) -> Autor:
    if autores.get(id, 0):
        return autores.get(id)
    else:
        raise RegistroNaoEncontradoException("Registro não encontrado")


def cadastrar(autor: Autor) -> None:
    autores[autor.id] = autor


def editar(id: int, nome: str, bio: str) -> Autor:
    autor = listar_por_id(id)
    autor.nome = nome
    autor.biografia = bio
    return autor
