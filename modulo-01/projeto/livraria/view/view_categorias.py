from rich.console import Console
from dao.dao_categorias import CategoriaDAO
from model.model_categoria import Categoria
from exception.exceptions import RegistroNaoEncontradoException

console = Console()
dao_categorias = CategoriaDAO()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Categorias", align="center")
        console.print(
            "1 - Cadastrar\n"
            + "2 - Listar\n"
            + "3 - Listar por Id\n"
            + "4 - Editar\n"
            + "5 - Excluir\n"
            + "0 - Voltar"
        )
        console.rule(align="center")
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                cadastrar()
            case "2":
                listar()
                console.input("\nPressione enter para continuar...")
            case "3":
                listar_por_id()
            case "4":
                editar()
            case "5":
                excluir()
            case "0":
                break
            case _:
                console.input(
                    "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                )


def listar() -> None:
    mensagem = ""
    console.clear()
    console.rule(title="Listagem de categorias", align="center")
    try:
        categorias = dao_categorias.listar()
        console.print(f"{'Id'.rjust(2)} | {'Nome da categoria'.ljust(30)}")
        for categoria in categorias:
            console.print(
                f"{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
            )

    except RegistroNaoEncontradoException as e:
        mensagem += f"[red]Nenhuma categoria cadastrada."
    finally:
        console.print(f"{mensagem}")
        console.rule(align="center")


def excluir() -> None:
    listar()

    id = int(console.input("Entre com o id da categoria para excluir: "))
    categoria = dao_categorias.excluir(id)
    console.input(
        f"\nCategoria {categoria.nome} removida com sucesso."
        + f"\nPresione enter para continuar..."
    )


def editar():
    mensagem = ""
    try:
        listar()
        dao_categorias.listar()
        id = int(console.input("Informe o id da categoria para editar"))
        dao_categorias.listar_por_id(id)
        console.clear()
        console.rule(title="Listagem de Categorias", align="center")
        nome = console.input("\nInforme o nome dda categoria: ")

        categoria = dao_categorias.editar(id, nome)

        console.rule(align="center")
        mensagem += f"\nCategoria {categoria.nome} editada com sucesso. "

    except ValueError as e:
        mensagem += "\nValue inválido. Pressione enter para continuar..."
    except RegistroNaoEncontradoException as e:
        mensagem += "\n{e}"
    finally:
        console.print(f"{mensagem}")


def listar_por_id() -> None:
    try:
        listar()

        id = int(console.input("Entre com o id da categoria para excluir: "))

        categoria = dao_categorias.listar_por_id(id)

        console.clear()
        console.rule(title="Listagem de categoriaes", align="center")
        console.print(f"Id: {categoria.id}\n" + f"Nome: {categoria.nome}")
        console.rule(align="center")
        console.input("\nPressione enter para continuar...")
    except ValueError as e:
        mensagem += "\nValue inválido. Pressione enter para continuar..."
    except RegistroNaoEncontradoException as e:
        mensagem += "\n{e}"
    finally:
        console.print(f"{mensagem}")


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
