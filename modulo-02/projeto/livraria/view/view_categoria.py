from rich.console import Console
from dao.dao_categoria import CategoriaDAO
from controller.controller_categoria import CategoriaController
from exception.exceptions import RegistroNaoEncontradoException


class CategoriaView:
    def __init__(self):
        self.console = Console()
        self.controller = CategoriaController()

    def menu(self) -> None:
        while True:
            self.console.clear()
            self.console.rule(title="Menu Categorias", align="center")
            self.console.print(
                "1 - Cadastrar\n"
                + "2 - Listar\n"
                + "3 - Listar por Id\n"
                + "4 - Atualizar\n"
                + "5 - Excluir\n"
                + "0 - Voltar"
            )
            self.console.rule(align="center")
            opcao = self.console.input("\nInforme a opção desejada: ")
            match opcao:
                case "1":
                    self.inserir()
                case "2":
                    self.listar()
                case "3":
                    self.listar_por_id()
                case "4":
                    self.atualizar()
                case "5":
                    self.excluir()
                case "0":
                    break
                case _:
                    self.console.input(
                        "\n[red]Opção inválida. Pressione enter para " + "continuar... "
                    )


    def inserir(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Cadastro de Categorias", align="center")
        nome = self.console.input("Informe o nome da categoria: ")
        categoria_info = {"nome": nome}
        self.console.rule(align="center")

        resposta = self.controller.inserir(categoria_info)
        if resposta["success"]:
            message += f"\n[green]{resposta["message"]}."
        else:
            message += f"\n[red]Falha ao inserir categoria "
            message += f"\n{resposta["error"]}."

        self.console.input(f"{message}\nPressione enter para continuar...")


    def listar(self) -> None:
        message: str = ""
        resposta = self.controller.listar()

        self.console.clear()
        self.console.rule(title="Listagem de Categorias", align="center")

        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
            for categoria in resposta["message"]:
                message += (
                    f"\n{str(categoria.id).rjust(2)}" + f" | {categoria.nome.ljust(30)}"
                )
        else:
            message += f"[red]{resposta["error"]}"

        self.console.print(f"{message}")
        self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar...")


    def atualizar(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Categorias", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
            for categoria in resposta["message"]:
                message += (
                    f"\n{str(categoria[0]).rjust(2)}" + f" | {categoria[1].ljust(30)}"
                )

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id da categoria para editar: ")
            nome = self.console.input("Informe o nome da categoria: ")
            categoria_info = {"id": id, "nome": nome}

            # atualizar
            resposta = self.controller.atualizar(categoria_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Categoria atualizada com sucesso."
                )
            else:
                message = f"[red]Erro: {resposta["error"]}."
            self.console.input(f"{message}\nPressione enter para continuar.")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
            self.console.input(f"[red]\nPressione enter para continuar.")


    def excluir(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Categorias", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
            for categoria in resposta["message"]:
                message += (
                    f"\n{str(categoria[0]).rjust(2)}" + f" | {categoria[1].ljust(30)}"
                )

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do categoria para excluir: ")
            categoria_info = {"id": id}

            # atualizar
            resposta = self.controller.excluir(categoria_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Categoria excluído com sucesso."
                )
            else:
                message = f"[red]Erro: {resposta["error"]}."
            self.console.input(f"{message}\nPressione enter para continuar.")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
            self.console.input(f"[red]\nPressione enter para continuar.")


    def listar_por_id(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Categorias", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Categoria'.ljust(30)}"
            for categoria in resposta["message"]:
                message += (
                    f"\n{str(categoria[0]).rjust(2)}" + f" | {categoria[1].ljust(30)}"
                )

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id da categoria para listar: ")
            categoria_info = {"id": id}

            # atualizar
            resposta = self.controller.buscar_por_id(categoria_info)
            if resposta["success"]:
                message = f"Id: {resposta["message"][0]}\n"
                message += f"Nome: {resposta["message"][1]}\n"
            else:
                message = f"[red]Erro: {resposta["error"]}."

            self.console.clear()
            self.console.rule(title="Listagem de Categorias", align="center")
            self.console.print(f"{message}")
            self.console.rule(align="center")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar.")
