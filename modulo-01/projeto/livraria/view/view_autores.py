from rich.console import Console
from dao import dao_autores
from model.model_autor import Autor


console = Console()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
        console.print(
            "1 - Cadastrar\n"
            + "2 - Listar\n"
            + "3 - Listar por Id\n"
            + "4 - Editar\n"
            + "5 - Excluir\n"
            + "0 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                cadastrar()
            case "2":
                listar()
                console.input("\nPressione enter para continuar...")
            case "3":
                listar_por_id()
            case "4":
                editar()
            case "5":
                excluir()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar() -> None:
    autores = dao_autores.listar()

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

    dao_autores.cadastrar(autor)

    console.rule(align="center")
    console.input(
        "\nAutor cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def excluir() -> None:
    message: str = ""
    listar()
    console.input("\nPressione enter para continuar...")
    try:
        if dao_autores.listar():
            id = int(console.input("Entre com o id do autor para excluir: "))
            autor = dao_autores.excluir(id)
            message += (
                f"\nAutor {autor.nome} removido com sucesso."
                + f"\nPresione enter para continuar..."
            )
    except ValueError as e:
        message = f"Valor inserido incorreto\n{e} \nPresione enter para continuar..."
    finally:
        console.print(message)


def listar_por_id() -> None:
    listar()

    id = int(console.input("Entre com o id do autores para listar: "))
    autor = dao_autores.listar_por_id(id)
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    console.print(
        f"Id: {autor.id}\n" + f"Nome: {autor.nome}\n" + f"Biografia: {autor.biografia}"
    )
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def editar() -> None:
    listar()

    id = int(console.input("Entre com o id do autores para editar: "))

    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor = Autor(nome, bio)

    _autor = dao_autores.editar(id, autor)

    console.rule(align="center")
    console.input(
        f"\nAutor {_autor.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
