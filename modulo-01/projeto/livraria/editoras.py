from rich.console import Console
from models.model import Editora

console = Console()


def menu_editoras(editoras: list[Editora]) -> None:
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
                listar_editoras(editoras)
            case "2":
                cadastrar_editoras(editoras)
            case "3":
                excluir_editoras(editoras)
            case "4":
                listar_editora_por_id(editoras)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar_editoras(editoras: list[Editora]) -> None:
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


def excluir_editoras(editoras: list[Editora]) -> None:
    console.clear()
    console.rule(title="Listagem de Editoras", align="center")
    if editoras:
        console.print(f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}")
        for editora in editoras:
            console.print(
                f"{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhum editora cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do editoras para excluir: "))
    for idx, editora in enumerate(editoras):
        if editora.id == id:
            break
    editora = editoras.pop(idx)
    console.input(
        f"\nEditora {editora.nome} removido com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_editora_por_id(editoras: list[Editora]) -> None:
    console.clear()
    console.rule(title="Listagem de Editoras", align="center")
    if editoras:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Editora'.ljust(30)}")
        for editora in editoras:
            console.print(
                f"{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhum editora cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do editoras para excluir: "))
    for idx, editora in enumerate(editoras):
        if editora.id == id:
            break

    editora = editoras[idx]
    console.clear()
    console.rule(title="Listagem de editoraes", align="center")
    console.print(f"Id: {editora.id}\n" + f"Nome: {editora.nome}")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar_editoras(editoras: list[Editora]) -> None:
    console.clear()
    console.rule(title="Cadastro de editoras", align="center")
    nome = console.input("\nInforme o nome do editora: ")
    editora = Editora(nome=nome)
    editoras.append(editora)
    console.rule(align="center")
    console.input(
        "\nEditora cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def editar_editora(editoras: list[Editora]) -> None:
    console.clear()
    console.rule(title="Listagem de editoras", align="center")
    if editoras:
        console.print(f"{'Id'.rjust(2)} | {'Nome do editora'.ljust(30)}")
        for editora in editoras:
            console.print(
                f"{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma editora cadastrada.")
    console.rule(align="center")

    id = int(console.input("Entre com o id da editoras para excluir: "))
    for idx, editora in enumerate(editoras):
        if editora.id == id:
            break

    editora = editoras[idx]
    console.clear()
    console.rule(title="Listagem de editoraes", align="center")
    nome = console.input("\nInforme o nome da editora: ")
    editora.nome = nome
    console.rule(align="center")
    console.input(
        f"\nEditora {editora.nome} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
