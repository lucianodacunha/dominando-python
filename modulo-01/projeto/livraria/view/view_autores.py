from rich.console import Console

from dao import dao_autores
from model.model_autor import Autor


console = Console()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
        console.print(
            "1 - Listar\n"
            + "2 - Cadastrar\n"
            + "3 - Excluir\n"
            + "4 - Editar\n"
            + "5 - Listar por Id\n"
            + "6 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                listar()
                console.input("\nPressione enter para continuar...")
            case "2":
                cadastrar()
            case "3":
                excluir()
            case "4":
                editar()
            case "5":
                listar_por_id()
            case "6":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar() -> None:
    autores = dao_autores.listar_autores()

    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")


def cadastrar() -> None:
    console.clear()
    console.rule(title="Cadastro de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor = Autor(nome=nome, biografia=bio)

    dao_autores.cadastrar_autores(autor)

    console.rule(align="center")
    console.input(
        "\nAutor cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def excluir() -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")

    autores = dao_autores.listar_autores()

    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do autores para excluir: "))
    # TODO: Implementar dict para facilitar a pesquisa por chave.

    autor = dao_autores.excluir(id)
    console.input(
        f"\nAutor {autor.nome} removido com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_por_id() -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    autores = dao_autores.listar_autores()
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do autores para excluir: "))
    autor = dao_autores.listar_autor_por_id(id)
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    console.print(
        f"Id: {autor.id}\n" + f"Nome: {autor.nome}\n" + f"Biografia: {autor.biografia}"
    )
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def editar() -> None:
    listar()

    id = int(console.input("Entre com o id do autores para excluir: "))

    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor = Autor(nome, bio)

    _autor = dao_autores.editar_autor(id, autor)

    console.rule(align="center")
    console.input(
        f"\nAutor {_autor.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
