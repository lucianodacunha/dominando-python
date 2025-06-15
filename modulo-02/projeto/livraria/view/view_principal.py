from rich.console import Console
from view.view_autor import AutorView
from view.view_categoria import CategoriaView
from view.view_editora import EditoraView
from view.view_livro import LivroView


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
                AutorView().menu()
            case "2":
                CategoriaView().menu()
            case "3":
                EditoraView().menu()
            case "4":
                LivroView().menu()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
