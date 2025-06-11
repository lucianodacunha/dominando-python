from rich.console import Console
from controller.controller_livro import LivroController

console = Console()
controller = LivroController()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Livros", align="center")
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
    console.rule(title="Cadastro de Livros", align="center")
    titulo = console.input("Informe o titulo do livro: ")
    resumo = console.input("Informe o resumo do livro: ")
    ano = console.input("Informe o ano do livro: ")
    paginas = console.input("Informe as paginas do livro: ")
    isbn = console.input("Informe o isbn do livro: ")
    livro_info = {
        "titulo": titulo,
        "resumo": resumo,
        "ano": ano,
        "paginas": paginas,
        "isbn": isbn,
    }
    console.rule(align="center")

    resposta = controller.inserir(livro_info)
    if resposta["success"]:
        message += f"\n[green]{resposta["message"]}."
    else:
        message += f"\n[red]Falha ao inserir livro "
        message += f"\n{resposta["error"]}."

    console.input(f"{message}\nPressione enter para continuar...")


def listar() -> None:
    message: str = ""
    resposta = controller.listar()

    console.clear()
    console.rule(title="Listagem de Livros", align="center")

    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
        for livro in resposta["message"]:
            message += f"\n{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}"
    else:
        message += f"[red]{resposta["error"]}"

    console.print(f"{message}")
    console.rule(align="center")
    console.input(f"\nPressione enter para continuar...")


def atualizar() -> None:
    message: str = ""

    console.clear()
    console.rule(title="Listagem de Livros", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
        for livro in resposta["message"]:
            message += f"\n{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do livro para editar: ")
        titulo = console.input("Informe o titulo do livro: ")
        resumo = console.input("Informe o resumo do livro: ")
        ano = console.input("Informe o ano do livro: ")
        paginas = console.input("Informe as paginas do livro: ")
        isbn = console.input("Informe o isbn do livro: ")
        livro_info = {
            "id": id,
            "titulo": titulo,
            "resumo": resumo,
            "ano": ano,
            "paginas": paginas,
            "isbn": isbn,
        }

        # atualizar
        resposta = controller.atualizar(livro_info)
        if resposta["success"]:
            message = (
                f"\n[green]Livro {resposta["message"].titulo} atualizado com sucesso."
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
    console.rule(title="Listagem de Livros", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
        for livro in resposta["message"]:
            message += f"\n{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do livro para excluir: ")
        livro_info = {"id": id}

        # atualizar
        resposta = controller.excluir(livro_info)
        if resposta["success"]:
            message = (
                f"\n[green]Livro {resposta["message"].titulo} excluído com sucesso."
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
    console.rule(title="Listagem de Livros", align="center")

    # listar
    resposta = controller.listar()
    if resposta["success"]:
        message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
        for livro in resposta["message"]:
            message += f"\n{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}"

        console.print(f"{message}")
        console.rule(align="center")

        id = console.input("\nEntre com o id do livro para listar: ")
        livro_info = {"id": id}

        # atualizar
        resposta = controller.buscar_por_id(livro_info)
        if resposta["success"]:
            message = f"Id: {resposta["message"].id}\n"
            message += f"Titulo: {resposta["message"].titulo}\n"
            message += f"Resumo: {resposta["message"].resumo}\n"
            message += f"Ano: {resposta["message"].ano}\n"
            message += f"Paginas: {resposta["message"].paginas}\n"
            message += f"ISBN: {resposta["message"].isbn}"
        else:
            message = f"[red]Erro: {resposta["error"]}."

        console.clear()
        console.rule(title="Listagem de Livros", align="center")
        console.print(f"{message}")
        console.rule(align="center")
    else:
        message += f"[red]{resposta["error"]}"
        console.print(f"{message}")
        console.rule(align="center")
    console.input(f"\nPressione enter para continuar.")
