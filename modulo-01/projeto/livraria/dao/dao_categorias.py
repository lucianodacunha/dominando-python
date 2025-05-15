from rich.console import Console
from model.model_categoria import Categoria

console = Console()


def listar_categorias(categorias: list[Categoria]) -> None:
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    if categorias:
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma categoria cadastrada.")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def excluir_categorias(categorias: list[Categoria]) -> None:
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    if categorias:
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma categoria cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id da categoria para excluir: "))
    for idx, categoria in enumerate(categorias):
        if categoria.id == id:
            break
    categoria = categorias.pop(idx)
    console.input(
        f"\nCategoria {categoria.nome} removida com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_categoria_por_id(categorias: list[Categoria]) -> None:
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    if categorias:
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma categoria cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id da categoria para excluir: "))
    for idx, categoria in enumerate(categorias):
        if categoria.id == id:
            break

    categoria = categorias[idx]
    console.clear()
    console.rule(title="Listagem de categoriaes", align="center")
    console.print(f"Id: {categoria.id}\n" + f"Nome: {categoria.nome}")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar_categorias(categorias: list[Categoria]) -> None:
    console.clear()
    console.rule(title="Cadastro de categorias", align="center")
    nome = console.input("\nInforme o nome da categoria: ")
    categoria = Categoria(nome=nome)
    categorias.append(categoria)
    console.rule(align="center")
    console.input(
        "\nCategoria cadastrada com sucesso. " "Pressione enter para continuar..."
    )


def editar_categoria(categorias: list[Categoria]) -> None:
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    if categorias:
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma categoria cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id da categoria para excluir: "))
    for idx, categoria in enumerate(categorias):
        if categoria.id == id:
            break

    categoria = categorias[idx]
    console.clear()
    console.rule(title="Listagem de categoriaes", align="center")
    nome = console.input("\nInforme o nome da categoria: ")
    categoria.nome = nome
    console.rule(align="center")
    console.input(
        f"\nCategoria {categoria.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
