from rich.console import Console
from model.model_editora import Editora

console = Console()
editoras: list[Editora] = list()


def listar() -> None:
    console.clear()
    console.rule(title="Listagem de editoras", align="center")
    if editoras:
        console.print(f"{'Id'.rjust(2)} | {'Nome da editora'.ljust(30)}")
        for editora in editoras:
            console.print(
                f"{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma editora cadastrada.")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def excluir(id: int) -> None:
    for idx, editora in enumerate(editoras):
        if editora.id == id:
            break
    return editoras.pop(idx)


def listar_por_id(id: int) -> None:
    for idx, editora in enumerate(editoras):
        if editora.id == id:
            break

    return editoras[idx]


def cadastrar(editora: Editora) -> None:
    editoras.append(editora)


def editar(id: int, editora: Editora) -> Editora:
    for idx, _editora in enumerate(editoras):
        if _editora.id == id:
            break

    _editora = editoras[idx]
    _editora.nome = editora.nome
    return _editora
