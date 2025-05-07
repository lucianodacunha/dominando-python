from rich.console import Console
from rich.prompt import Prompt


console = Console()


def main() -> None:

    categorias: list[str] = list()
    editoras: list[str] = list()
    autores: list[str] = list()
    livros: list[str] = list()

    while True:
        menu_principal()
        opcao = console.input("\nInforme a opção desejada: ")

        match opcao:
            case "1":
                menu_categorias()
            case "2":
                menu_editoras()
            case "3":
                menu_autores()
            case "4":
                menu_livros()
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                              "continuar... ")

    console.input("\n[red]Pressione enter para finalizar...")
    console.clear()


def menu_principal() -> None:
    console.clear()
    console.rule(title="Menu Principal", align="center")
    console.print("1 - Categorias")
    console.print("2 - Editoras")
    console.print("3 - Autores")
    console.print("4 - Livros")
    console.print("5 - Sair")
    console.rule(align="center")    


def menu_categorias() -> None:
    pass


def menu_editoras() -> None:
    pass


def menu_autores() -> None:
    pass


def menu_livros() -> None:
    pass


if __name__ == "__main__":
    main()
