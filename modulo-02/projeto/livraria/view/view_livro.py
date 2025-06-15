from rich.console import Console
from controller.controller_livro import LivroController


class LivroView:
    def __init__(self):
        self.console = Console()
        self.controller = LivroController()

    def menu(self) -> None:
        while True:
            self.console.clear()
            self.console.rule(title="Menu Livros", align="center")
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
        self.console.rule(title="Cadastro de Livros", align="center")
        titulo = self.console.input("Informe o titulo do livro: ")
        resumo = self.console.input("Informe o resumo do livro: ")
        ano = self.console.input("Informe o ano do livro: ")
        paginas = self.console.input("Informe as paginas do livro: ")
        isbn = self.console.input("Informe o isbn do livro: ")
        livro_info = {
            "titulo": titulo,
            "resumo": resumo,
            "ano": ano,
            "paginas": paginas,
            "isbn": isbn,
        }
        self.console.rule(align="center")

        resposta = self.controller.inserir(livro_info)
        if resposta["success"]:
            message += f"\n[green]{resposta["message"]}."
        else:
            message += f"\n[red]Falha ao inserir livro "
            message += f"\n{resposta["error"]}."

        self.console.input(f"{message}\nPressione enter para continuar...")


    def listar(self) -> None:
        message: str = ""
        resposta = self.controller.listar()

        self.console.clear()
        self.console.rule(title="Listagem de Livros", align="center")

        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
            for livro in resposta["message"]:
                message += f"\n{str(livro[0]).rjust(2)}" + f" | {livro[1].ljust(30)}"
        else:
            message += f"[red]{resposta["error"]}"

        self.console.print(f"{message}")
        self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar...")


    def atualizar(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Livros", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
            for livro in resposta["message"]:
                message += f"\n{str(livro[0]).rjust(2)}" + f" | {livro[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do livro para editar: ")
            titulo = self.console.input("Informe o titulo do livro: ")
            resumo = self.console.input("Informe o resumo do livro: ")
            ano = self.console.input("Informe o ano do livro: ")
            paginas = self.console.input("Informe as paginas do livro: ")
            isbn = self.console.input("Informe o isbn do livro: ")
            livro_info = {
                "id": id,
                "titulo": titulo,
                "resumo": resumo,
                "ano": ano,
                "paginas": paginas,
                "isbn": isbn,
            }

            # atualizar
            resposta = self.controller.atualizar(livro_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Livro atualizado com sucesso."
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
        self.console.rule(title="Listagem de Livros", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
            for livro in resposta["message"]:
                message += f"\n{str(livro[0]).rjust(2)}" + f" | {livro[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do livro para excluir: ")
            livro_info = {"id": id}

            # atualizar
            resposta = self.controller.excluir(livro_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Livro excluído com sucesso."
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
        self.console.rule(title="Listagem de Livros", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Titulo do Livro'.ljust(30)}"
            for livro in resposta["message"]:
                message += f"\n{str(livro[0]).rjust(2)}" + f" | {livro[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do livro para listar: ")
            livro_info = {"id": id}

            # atualizar
            resposta = self.controller.listar_por_id(livro_info)
            if resposta["success"]:
                message = f"Id: {resposta["message"][0]}\n"
                message += f"Titulo: {resposta["message"][1]}\n"
                message += f"Resumo: {resposta["message"][2]}\n"
                message += f"Ano: {resposta["message"][3]}\n"
                message += f"Paginas: {resposta["message"][4]}\n"
                message += f"ISBN: {resposta["message"][5]}"
            else:
                message = f"[red]Erro: {resposta["error"]}."

            self.console.clear()
            self.console.rule(title="Listagem de Livros", align="center")
            self.console.print(f"{message}")
            self.console.rule(align="center")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar.")
