from rich.console import Console
from model.model_categoria import Categoria

console = Console()
categorias: list[Categoria] = list()


def listar() -> None:
    return categorias


def excluir(id: int) -> None:
    for idx, categoria in enumerate(categorias):
        if categoria.id == id:
            break
    return categorias.pop(idx)


def listar_por_id(id: int) -> None:

    for idx, categoria in enumerate(categorias):
        if categoria.id == id:
            break

    return categorias[idx]


def cadastrar(categoria: Categoria) -> None:
    categorias.append(categoria)


def editar(id: int, categoria: Categoria) -> None:
    for idx, _categoria in enumerate(categorias):
        if _categoria.id == id:
            break

    _categoria = categorias[idx]
    _categoria.nome = categoria.nome

    console.rule(align="center")
    console.input(
        f"\nCategoria {_categoria.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
