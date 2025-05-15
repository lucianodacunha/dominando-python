from rich.console import Console

from dao import dao_editoras
from model.model_editora import Editora

console = Console()


def menu_editoras(editoras: list[Editora]) -> None:
    while True:
        console.clear()
        console.rule(title="Menu Editoras", align="center")
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
                dao_editoras.listar_editoras(editoras)
            case "2":
                dao_editoras.cadastrar_editoras(editoras)
            case "3":
                dao_editoras.excluir_editoras(editoras)
            case "4":
                dao_editoras.listar_editora_por_id(editoras)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
