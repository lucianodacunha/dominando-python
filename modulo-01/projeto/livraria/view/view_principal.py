from rich.console import Console
from view import view_autores
from view import view_categorias
from view import view_editoras
from view import view_livros


console = Console()


def menu() -> None:

    while True:
        console.clear()
        console.rule(title="Menu Principal", align="center")
        console.print(
            "1 - Autores\n"
            + "2 - Categorias\n"
            + "3 - Editoras\n"
            + "4 - Livros\n"
            + "0 - Sair"
        )
        console.rule(align="center")

        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                view_autores.menu()
            case "2":
                view_categorias.menu()
            case "3":
                view_editoras.menu()
            case "4":
                view_livros.menu()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
