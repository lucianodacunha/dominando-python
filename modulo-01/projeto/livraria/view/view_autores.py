from rich.console import Console

from dao import dao_autores
from model.model_autor import Autor


console = Console()


def menu_autores(autores: list[Autor]) -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
        console.print(
            "1 - Listar\n"
            + "2 - Cadastrar\n"
            + "3 - Excluir\n"
            + "4 - Editar\n"
            + "5 - Listar por Id\n"
            + "6 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                dao_autores.listar_autores(autores)
            case "2":
                dao_autores.cadastrar_autores(autores)
            case "3":
                dao_autores.excluir_autores(autores)
            case "4":
                dao_autores.editar_autor(autores)
            case "5":
                dao_autores.listar_autor_por_id(autores)
            case "6":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
