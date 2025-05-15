from rich.console import Console
from model.model_livro import Livro

console = Console()


def listar_livros(livros: list[Livro]) -> None:
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Título do Autor'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
    else:
        console.print("[red]Nenhum livro cadastrado.")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar_livros(livros: list[Livro]) -> None:
    console.clear()
    console.rule(title="Cadastro de Livros", align="center")
    titulo = console.input("\nInforme o titulo do livro: ")
    resumo = console.input("Informe um resumo do livro: ")
    ano = console.input("Informe o ano do livro: ")
    paginas = console.input("Informe a qtde. paginas do livro: ")
    isbn = console.input("Informe o isbn do livro: ")
    livro = Livro(titulo=titulo, resumo=resumo, ano=ano, paginas=paginas, isbn=isbn)
    livros.append(livro)
    console.rule(align="center")
    console.input(
        "\nLivro cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def excluir_livro(livros: list[Livro]) -> None:
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Título do Livro'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
        console.rule(align="center")

        id = int(console.input("Entre com o id do livros para excluir: "))
        for idx, livro in enumerate(livros):
            if livro.id == id:
                break
        livro = livros.pop(idx)
        console.input(
            f"\nLivro {livro.titulo} removido com sucesso."
            + f"\nPresione enter para continuar..."
        )
    else:
        console.print("[red]Nenhum livro cadastrado.")
        console.rule(align="center")
        console.input(f"\nPresione enter para continuar...")


def listar_livro_por_id(livros: list[Livro]) -> None:
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Livro'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
    else:
        console.print("[red]Nenhum livro cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do livros para excluir: "))
    for idx, livro in enumerate(livros):
        if livro.id == id:
            break

    livro = livros[idx]
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


def editar_livro(livros: list[Livro]) -> None:
    console.clear()
    console.rule(title="Listagem de Livro", align="center")
    if livros:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Livro'.ljust(30)}")
        for livro in livros:
            console.print(f"{str(livro.id).rjust(2)}" + f" | {livro.titulo.ljust(30)}")
    else:
        console.print("[red]Nenhum livro cadastrado.")
    console.rule(align="center")

    id = int(console.input("Entre com o id do livros para excluir: "))
    for idx, livro in enumerate(livros):
        if livro.id == id:
            break

    livro = livros[idx]
    console.clear()
    console.rule(title="Listagem de Livros", align="center")
    titulo = console.input("\nInforme o nome do livro: ")
    resumo = console.input("Informe o resumo do livro: ")
    livro.titulo = titulo
    livro.resumo = resumo
    console.rule(align="center")
    console.input(
        f"\nLivro {livro.titulo} editado com sucesso. "
        + f"\nPressione enter para continuar..."
    )
