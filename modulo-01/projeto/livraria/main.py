from rich.console import Console
from models.model import Autor, Categoria, Editora, Livro
from autores import menu_autores
from categorias import menu_categorias
from editoras import menu_editoras
from livros import menu_livros

console = Console()


def main() -> None:

    menu_principal()
    console.input("\n[red]Pressione enter para finalizar...")
    console.clear()


def menu_principal() -> None:

    editoras: list[Editora] = list()
    autores: list[Autor] = list()
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
                menu_categorias(categorias)
            case "2":
                menu_editoras(editoras)
            case "3":
                menu_autores(autores)
            case "4":
                menu_livros(livros)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


if __name__ == "__main__":
    main()
