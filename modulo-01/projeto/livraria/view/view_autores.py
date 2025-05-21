from rich.console import Console
from dao.dao_autores import Autor_DAO
from model.model_autor import Autor
from exception.exceptions import RegistroNaoEncontradoException

console = Console()
dao_autores = Autor_DAO()


def menu() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
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
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    try:
        autores = dao_autores.listar()
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + f" | {autor.nome.ljust(30)}")
    except RegistroNaoEncontradoException as e:
        console.print(f"[red]{e}")
    console.rule(align="center")


def cadastrar() -> None:
    console.clear()
    console.rule(title="Cadastro de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor = Autor(nome, bio)

    dao_autores.cadastrar(autor)

    console.rule(align="center")
    console.input(
        "\nAutor cadastrado com sucesso. " "Pressione enter para continuar..."
    )


def excluir() -> None:
    mensagem: str = ""
    try:
        listar()
        dao_autores.listar()
        id = int(console.input("Entre com o id do autor para excluir: "))
        autor = dao_autores.excluir(id)
        mensagem += (
            f"\nAutor {autor.nome} removido com sucesso."
            + f"\nPresione enter para continuar..."
        )
    except ValueError as e:
        mensagem = f"\nValor inválido \nPressione enter para continuar..."
    except RegistroNaoEncontradoException as e:
        mensagem = f"\n{e} \nPressione enter para continuar..."
    finally:
        console.input(f"[red]{mensagem}")


def listar_por_id() -> None:
    mensagem: str = ""
    listar()
    try:
        dao_autores.listar()
        id = int(console.input("Entre com o id do autor para listar: "))
        autor = dao_autores.listar_por_id(id)
        console.clear()
        console.rule(title="Listagem de Autores", align="center")
        console.print(
            f"Id: {autor.id}\n"
            + f"Nome: {autor.nome}\n"
            + f"Biografia: {autor.biografia}"
        )
        console.rule(align="center")
        mensagem += f"\nPressione enter para continuar..."
    except ValueError as e:
        mensagem = f"\nValor inválido \nPressione enter para continuar..."
    except RegistroNaoEncontradoException as e:
        mensagem += f"\n{e}\nPressione enter para continuar..."
    finally:
        console.input(f"[red]{mensagem} ")


def editar() -> None:
    mensagem: str = ""
    listar()
    try:
        dao_autores.listar()
        id = int(console.input("Entre com o id do autor para editar: "))
        autor = dao_autores.listar_por_id(id)
        console.clear()
        console.rule(title="Listagem de Autores", align="center")
        nome = console.input("\nInforme o nome do autor: ")
        bio = console.input("Informe a biografia do autor: ")

        autor = dao_autores.editar(id, nome, bio)

        console.rule(align="center")
        mensagem += f"\nAutor {autor.nome} editado com sucesso. "
    except ValueError as e:
        mensagem = f"\nValor inválido \nPressione enter para continuar..."
    except RegistroNaoEncontradoException as e:
        mensagem += f"\n{e}\nPressione enter para continuar..."
    finally:
        console.input(f"{mensagem}")
