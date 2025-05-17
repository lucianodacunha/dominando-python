from rich.console import Console
from dao import dao_editoras
from model.model_editora import Editora

console = Console()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Editoras", align="center")
        console.print(
            "1 - Listar\n"
            + "2 - Cadastrar\n"
            + "3 - Excluir\n"
            + "4 - Listar por Id\n"
            + "5 - Voltar"
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
                listar_por_id()
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar() -> None:
    editoras = dao_editoras.listar()

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


def excluir(id: int) -> None:
    listar()

    id = int(console.input("Entre com o id da editora para excluir: "))

    editora = dao_editoras.excluir(id)
    console.input(
        f"\nEditora {editora.nome} removido com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_por_id() -> None:
    listar()

    id = int(console.input("Entre com o id da editoras para listar: "))
    editora = dao_editoras.listar_por_id(id)
    console.clear()
    console.rule(title="Listagem de editora", align="center")
    console.print(f"Id: {editora.id}\n" + f"Nome: {editora.nome}")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar() -> None:
    console.clear()
    console.rule(title="Cadastro de editoras", align="center")
    nome = console.input("\nInforme o nome do editora: ")
    editora = Editora(nome=nome)
    dao_editoras.cadastrar(editora)
    console.rule(align="center")
    console.input(
        "\nEditora cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def editar() -> Editora:
    listar()

    id = int(console.input("Entre com o id da editora para editar: "))

    editora = dao_editoras.listar_por_id(id)
    console.clear()
    console.rule(title="Listagem de editora", align="center")
    nome = console.input("\nInforme o nome da editora: ")
    editora.nome = nome
    console.rule(align="center")
    console.input(
        f"\nEditora {editora.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
