from rich.console import Console

from model.model_categoria import Categoria
from model.model_editora import Editora
from model.model_livro import Livro
from view import view_autores
from view import view_categorias
from view import view_editoras
from view import view_livros


console = Console()


def menu_principal() -> None:

    editoras: list[Editora] = list()
    livros: list[Livro] = list()
    categorias: list[Categoria] = list()

    while True:
        console.clear()
        console.rule(title="Menu Principal", align="center")
        console.print(
            "1 - Categorias\n"
            + "2 - Editoras\n"
            + "3 - Autores\n"
            + "4 - Livros\n"
            + "5 - Sair"
        )
        console.rule(align="center")

        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                view_autores.menu()
            case "2":
                view_categorias.menu_categorias(categorias)
            case "3":
                view_editoras.menu_editoras(editoras)
            case "4":
                view_livros.menu_livros(livros)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
