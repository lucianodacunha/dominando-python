from rich.console import Console
from dao import dao_categorias
from model.model_categoria import Categoria

console = Console()


def menu_categorias(categorias: list[Categoria]) -> None:
    while True:
        console.clear()
        console.rule(title="Menu Categorias", align="center")
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
                dao_categorias.listar_categorias(categorias)
            case "2":
                dao_categorias.cadastrar_categorias(categorias)
            case "3":
                dao_categorias.excluir_categorias(categorias)
            case "4":
                dao_categorias.listar_categoria_por_id(categorias)
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )
