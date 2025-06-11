from rich.console import Console
from dao.dao_categoria import CategoriaDAO
from controller.controller_categoria import CategoriaController
from exception.exceptions import RegistroNaoEncontradoException

console = Console()
controller = CategoriaController()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Categorias", align="center")
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
    console.rule(title="Cadastro de Categorias", align="center")
    nome = console.input("Informe o nome da categoria: ")
    categoria_info = {"nome": nome}
    console.rule(align="center")

    resposta = controller.inserir(categoria_info)
    if resposta["success"]:
        message += f"\n[green]{resposta["message"]}."
    else:
        message += f"\n[red]Falha ao inserir categoria "
        message += f"\n{resposta["error"]}."

    console.input(f"{message}\nPressione enter para continuar...")


def listar() -> None:
    message: str = ""
    resposta = controller.listar()

    console.clear()
    console.rule(title="Listagem de Categorias", align="center")

    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
        for categoria in resposta["message"]:
            message += (
                f"\n{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        message += f"[red]{resposta["error"]}"

    console.print(f"{message}")
    console.rule(align="center")
    console.input(f"\nPressione enter para continuar...")


def atualizar() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Categorias", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
        for categoria in resposta["message"]:
            message += (
                f"\n{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id da categoria para editar: ")
        nome = console.input("Informe o nome da categoria: ")
        categoria_info = {"id": id, "nome": nome}

        # atualizar
        resposta = controller.atualizar(categoria_info)
        if resposta["success"]:
            message = (
                f"\n[green]Categoria {resposta["message"].nome} atualizada com sucesso."
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
    console.rule(title="Listagem de Categorias", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
        for categoria in resposta["message"]:
            message += (
                f"\n{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do categoria para excluir: ")
        categoria_info = {"id": id}

        # atualizar
        resposta = controller.excluir(categoria_info)
        if resposta["success"]:
            message = (
                f"\n[green]Categoria {resposta["message"].nome} excluído com sucesso."
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
    console.rule(title="Listagem de Categorias", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
        for categoria in resposta["message"]:
            message += (
                f"\n{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id da categoria para listar: ")
        categoria_info = {"id": id}

        # atualizar
        resposta = controller.buscar_por_id(categoria_info)
        if resposta["success"]:
            message = f"Id: {resposta["message"].id}\n"
            message += f"Nome: {resposta["message"].nome}\n"
        else:
            message = f"[red]Erro: {resposta["error"]}."

        console.clear()
        console.rule(title="Listagem de Categorias", align="center")
        console.print(f"{message}")
        console.rule(align="center")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
    console.input(f"\nPressione enter para continuar.")
