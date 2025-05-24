from rich.console import Console
from exception.exceptions import RegistroNaoEncontradoException

from controller.controller_autor import AutorController

console = Console()
controller = AutorController()


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
    console.rule(title="Cadastro de Autores", align="center")
    nome = console.input("Informe o nome do autor: ")
    biografia = console.input("Informe a biografia do autor: ")
    autor_info = {"nome": nome, "biografia": biografia}
    console.rule(align="center")

    resposta = controller.inserir(autor_info)
    if resposta["success"]:
        message += f"\n[green]{resposta["message"]}."
    else:
        message += f"\n[red]Falha ao inserir autor "
        message += f"\n{resposta["error"]}."

    console.input(f"{message}\nPressione enter para continuar...")


def listar() -> None:
    message: str = ""
    resposta = controller.listar()

    console.clear()
    console.rule(title="Listagem de Autores", align="center")

    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
        for autor in resposta["message"]:
            message += f"\n{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}"
    else:
        message += f"[red]{resposta["error"]}"

    console.print(f"{message}")
    console.rule(align="center")
    console.input(f"\nPressione enter para continuar...")


def atualizar() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Autores", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
        for autor in resposta["message"]:
            message += f"\n{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do autor para editar: ")
        nome = console.input("Informe o nome do autor: ")
        biografia = console.input("Informe a biografia do autor: ")
        autor_info = {"id": id, "nome": nome, "biografia": biografia}

        # atualizar
        resposta = controller.atualizar(autor_info)
        if resposta["success"]:
            message = (
                f"\n[green]Autor {resposta["message"].nome} atualizado com sucesso."
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
    console.rule(title="Listagem de Autores", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
        for autor in resposta["message"]:
            message += f"\n{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do autor para excluir: ")
        autor_info = {"id": id}

        # atualizar
        resposta = controller.excluir(autor_info)
        if resposta["success"]:
            message = f"\n[green]Autor {resposta["message"].nome} excluído com sucesso."
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
    console.rule(title="Listagem de Autores", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
        for autor in resposta["message"]:
            message += f"\n{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do autor para listar: ")
        autor_info = {"id": id}

        # atualizar
        resposta = controller.buscar_por_id(autor_info)
        if resposta["success"]:
            message = f"Id: {resposta["message"].id}\n"
            message += f"Nome: {resposta["message"].nome}\n"
            message += f"Biografia: {resposta["message"].biografia}"
        else:
            message = f"[red]Erro: {resposta["error"]}."

        console.clear()
        console.rule(title="Listagem de Autores", align="center")
        console.print(f"{message}")
        console.rule(align="center")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
    console.input(f"\nPressione enter para continuar.")
