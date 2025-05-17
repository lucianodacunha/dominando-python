from rich.console import Console
from dao import dao_categorias
from model.model_categoria import Categoria

console = Console()


def menu() -> None:
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
                listar()
                console.input("\nPressione enter para continuar...")
            case "2":
                cadastrar()
            case "3":
                excluir()
            case "4":
                listar()
            case "5":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar() -> None:
    categorias = dao_categorias.listar()
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    if categorias:
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )
    else:
        console.print("[red]Nenhuma categoria cadastrada.")
    console.rule(align="center")


def excluir() -> None:
    listar()

    id = int(console.input("Entre com o id da categoria para excluir: "))
    categoria = dao_categorias.excluir(id)
    console.input(
        f"\nCategoria {categoria.nome} removida com sucesso."
        + f"\nPresione enter para continuar..."
    )


def listar_categoria_por_id() -> None:
    listar()

    id = int(console.input("Entre com o id da categoria para excluir: "))

    categoria = dao_categorias.listar_por_id(id)

    console.clear()
    console.rule(title="Listagem de categoriaes", align="center")
    console.print(f"Id: {categoria.id}\n" + f"Nome: {categoria.nome}")
    console.rule(align="center")
    console.input("\nPressione enter para continuar...")


def cadastrar() -> None:
    console.clear()
    console.rule(title="Cadastro de categorias", align="center")
    nome = console.input("\nInforme o nome da categoria: ")
    categoria = Categoria(nome=nome)

    dao_categorias.cadastrar(categoria)

    console.rule(align="center")
    console.input(
        "\nCategoria cadastrada com sucesso. " "Pressione enter para continuar..."
    )
