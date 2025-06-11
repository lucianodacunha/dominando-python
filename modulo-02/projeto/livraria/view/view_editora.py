from rich.console import Console
from controller.controller_editora import EditoraController

console = Console()
controller = EditoraController()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Editoras", align="center")
        console.print(
            "1 - Cadastrar\n"
            + "2 - Listar\n"
            + "3 - Listar por Id\n"
            + "4 - Atualizar\n"
            + "5 - Excluir\n"
            + "0 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                inserir()
            case "2":
                listar()
            case "3":
                listar_por_id()
            case "4":
                atualizar()
            case "5":
                excluir()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def inserir() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Cadastro de Editoras", align="center")
    nome = console.input("Informe o nome do editora: ")
    editora_info = {"nome": nome}
    console.rule(align="center")

    resposta = controller.inserir(editora_info)
    if resposta["success"]:
        message += f"\n[green]{resposta["message"]}."
    else:
        message += f"\n[red]Falha ao inserir editora "
        message += f"\n{resposta["error"]}."

    console.input(f"{message}\nPressione enter para continuar...")


def listar() -> None:
    message: str = ""
    resposta = controller.listar()

    console.clear()
    console.rule(title="Listagem de Editoras", align="center")

    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
        for editora in resposta["message"]:
            message += f"\n{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"
    else:
        message += f"[red]{resposta["error"]}"

    console.print(f"{message}")
    console.rule(align="center")
    console.input(f"\nPressione enter para continuar...")


def atualizar() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Editoras", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
        for editora in resposta["message"]:
            message += f"\n{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id da editora para editar: ")
        nome = console.input("Informe o nome da editora: ")
        editora_info = {"id": id, "nome": nome}

        # atualizar
        resposta = controller.atualizar(editora_info)
        if resposta["success"]:
            message = (
                f"\n[green]Editora {resposta["message"].nome} atualizada com sucesso."
            )
        else:
            message = f"[red]Erro: {resposta["error"]}."
        console.input(f"{message}\nPressione enter para continuar.")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
        console.input(f"[red]\nPressione enter para continuar.")


def excluir() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Editoras", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
        for editora in resposta["message"]:
            message += f"\n{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id da editora para excluir: ")
        editora_info = {"id": id}

        # atualizar
        resposta = controller.excluir(editora_info)
        if resposta["success"]:
            message = (
                f"\n[green]Editora {resposta["message"].nome} excluída com sucesso."
            )
        else:
            message = f"[red]Erro: {resposta["error"]}."
        console.input(f"{message}\nPressione enter para continuar.")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
        console.input(f"[red]\nPressione enter para continuar.")


def listar_por_id() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Editoras", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
        for editora in resposta["message"]:
            message += f"\n{str(editora.id).rjust(2)}" + f" | {editora.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id da editora para listar: ")
        editora_info = {"id": id}

        # atualizar
        resposta = controller.buscar_por_id(editora_info)
        if resposta["success"]:
            message = f"Id: {resposta["message"].id}\n"
            message += f"Nome: {resposta["message"].nome}\n"
        else:
            message = f"[red]Erro: {resposta["error"]}."

        console.clear()
        console.rule(title="Listagem de Editoras", align="center")
        console.print(f"{message}")
        console.rule(align="center")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
    console.input(f"\nPressione enter para continuar.")
