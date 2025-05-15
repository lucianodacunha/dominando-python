from rich.console import Console
from model.model_autor import Autor

console = Console()


def listar_autores(autores: list[Autor]) -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def excluir_autores(autores: list[Autor]) -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break
    autor = autores.pop(idx)
    console.input(
        f"\nAutor {autor.nome} removido com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_autor_por_id(autores: list[Autor]) -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break

    autor = autores[idx]
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    console.print(
        f"Id: {autor.id}\n" + f"Nome: {autor.nome}\n" + f"Biografia: {autor.biografia}"
    )
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar_autores(autores: list[Autor]) -> None:
    console.clear()
    console.rule(title="Cadastro de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor = Autor(nome=nome, biografia=bio)
    autores.append(autor)
    console.rule(align="center")
    console.input(
        "\nAutor cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def editar_autor(autores: list[Autor]) -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break

    autor = autores[idx]
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor.nome = nome
    autor.biografia = bio
    console.rule(align="center")
    console.input(
        f"\nAutor {autor.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
