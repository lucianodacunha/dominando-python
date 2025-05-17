from rich.console import Console

from dao import dao_livros
from model.model_livro import Livro

console = Console()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Livros", align="center")
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
    livros = dao_livros.listar()
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Título do Autor'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
    else:
        console.print("[red]Nenhum livro cadastrado.")
    console.rule(align="center")


def cadastrar() -> None:
    console.clear()
    console.rule(title="Cadastro de Livros", align="center")
    titulo = console.input("\nInforme o titulo do livro: ")
    resumo = console.input("Informe um resumo do livro: ")
    ano = console.input("Informe o ano do livro: ")
    paginas = console.input("Informe a qtde. paginas do livro: ")
    isbn = console.input("Informe o isbn do livro: ")
    livro = Livro(titulo=titulo, resumo=resumo, ano=ano, paginas=paginas, isbn=isbn)

    dao_livros.cadastrar(livro)

    console.rule(align="center")
    console.input(
        "\nLivro cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def excluir() -> None:
    listar()

    id = int(console.input("Entre com o id do livros para excluir: "))

    livro = dao_livros.excluir(id)

    console.input(
        f"\nLivro {livro.titulo} removido com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_por_id() -> None:
    listar()

    id = int(console.input("Entre com o id do livro para listar: "))
    livro = dao_livros.listar_por_id(id)
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    console.print(
        f"Id: {livro.id}\n"
        + f"Titulo: {livro.titulo}\n"
        + f"Resumo: {livro.resumo}\n"
        + f"Ano: {livro.ano}\n"
        + f"Páginas: {livro.paginas}\n"
        + f"ISBN: {livro.isbn}\n"
    )
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def editar() -> None:
    livros = dao_livros.listar()
    console.clear()
    console.rule(title="Listagem de Livro", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Livro'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
    else:
        console.print("[red]Nenhum livro cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do livros para editar: "))

    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    titulo = console.input("\nInforme o nome do livro: ")
    resumo = console.input("Informe o resumo do livro: ")
    _livro = Livro(titulo, resumo)
    _livro = dao_livros.editar(id, _livro)
    console.rule(align="center")
    console.input(
        f"\nLivro {_livro.titulo} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
