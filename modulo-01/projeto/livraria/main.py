from rich.console import Console
from rich.prompt import Prompt


console = Console()


def main() -> None:

    categorias: list[str] = list()
    editoras: list[str] = list()
    autores: list[str] = list()
    livros: list[str] = list()
    
    menu_principal()
    console.input("\n[red]Pressione enter para finalizar...")
    console.clear()


def menu_principal() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Principal", align="center")

        console.print("1 - Categorias\n" +
                    "2 - Editoras\n" +
                    "3 - Autores\n" + 
                    "4 - Livros\n" +
                    "5 - Sair")
        console.rule(align="center")   

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


def menu_categorias() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Categorias", align="center")
        console.print("1 - Listar\n" +
                    "2 - Cadastrar\n" +
                    "3 - Excluir\n" + 
                    "4 - Listar por Id\n" +
                    "5 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")



def menu_editoras() -> None:
    pass


def menu_autores() -> None:
    pass


def menu_livros() -> None:
    pass


if __name__ == "__main__":
    main()
