from rich.console import Console
from view import view_autor
from view import view_categoria
from view.view_editora import EditoraView
from view import view_livro


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
                view_autor.menu()
            case "2":
                view_categoria.menu()
            case "3":
                EditoraView().menu()
            case "4":
                view_livro.menu()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
