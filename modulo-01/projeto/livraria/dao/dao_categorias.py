from rich.console import Console
from model.model_categoria import Categoria
from exception.exceptions import RegistroNaoEncontradoException

categorias: dict[int, Categoria] = dict()
sequence = 1


def listar() -> list[Categoria]:
    if not categorias:
        raise RegistroNaoEncontradoException("Nenhum registro encontrado")
    return categorias.values()


def excluir(id: int) -> Categoria:
    if not categorias.get(id, 0):
        raise RegistroNaoEncontradoException("Registro não encontrado")
    return categorias.pop(id)


def listar_por_id(id: int) -> Categoria:
    if not categorias.get(id, 0):
        raise RegistroNaoEncontradoException("Registro não encontrado")
    return categorias.get(id)


def cadastrar(categoria: Categoria) -> None:
    global sequence
    categoria.id = sequence
    categorias.append(categoria)
    sequence += 1


def editar(id: int, nome: str) -> None:
    if not categorias.get(id, 0):
        raise RegistroNaoEncontradoException("Registro não encontrado")

    categoria = categorias.get(id)
    categoria.nome = categoria.nome
    return categoria
