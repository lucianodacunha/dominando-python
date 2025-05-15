from rich.console import Console

from dao import dao_livros
from model.model_livro import Livro

console = Console()


def menu_livros(livros: list[Livro]) -> None:
    while True:
        console.clear()
        console.rule(title="Menu Livros", align="center")
        console.print(
            "1 - Listar\n"
            + "2 - Cadastrar\n"
            + "3 - Excluir\n"
            + "4 - Listar por Id\n"
            + "5 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                dao_livros.listar_livros(livros)
            case "2":
                dao_livros.cadastrar_livros(livros)
            case "3":
                dao_livros.excluir_livro(livros)
            case "4":
                dao_livros.listar_livro_por_id(livros)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
