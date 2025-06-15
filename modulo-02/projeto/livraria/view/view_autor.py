from rich.console import Console
from controller.controller_autor import AutorController


class AutorView:
    def __init__(self):
        self.console = Console()
        self.controller = AutorController()

    def menu(self) -> None:
        while True:
            self.console.clear()
            self.console.rule(title="Menu Autores", align="center")
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
        self.console.rule(title="Cadastro de Autores", align="center")
        nome = self.console.input("Informe o nome do autor: ")
        email = self.console.input("Informe o email do autor: ")
        telefone = self.console.input("Informe o telefone do autor: ")
        bio = self.console.input("Informe a bio do autor: ")
        autor_info = {"nome": nome, "email": email, "telefone": telefone, "bio": bio}
        self.console.rule(align="center")

        resposta = self.controller.inserir(autor_info)
        if resposta["success"]:
            message += f"\n[green]{resposta["message"]}."
        else:
            message += f"\n[red]Falha ao inserir autor "
            message += f"\n{resposta["error"]}."

        self.console.input(f"{message}\nPressione enter para continuar...")


    def listar(self) -> None:
        message: str = ""
        resposta = self.controller.listar()

        self.console.clear()
        self.console.rule(title="Listagem de Autores", align="center")

        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
            for autor in resposta["message"]:
                message += f"\n{str(autor[0]).rjust(2)}" + f" | {autor[1].ljust(30)}"
        else:
            message += f"[red]{resposta["error"]}"

        self.console.print(f"{message}")
        self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar...")


    def atualizar(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Autores", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
            for autor in resposta["message"]:
                message += f"\n{str(autor[0]).rjust(2)}" + f" | {autor[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do autor para editar: ")
            nome = self.console.input("Informe o nome do autor: ")
            email = self.console.input("Informe o email do autor: ")
            telefone = self.console.input("Informe o telefone do autor: ")
            bio = self.console.input("Informe a bio do autor: ")
            autor_info = {"id": id, "nome": nome, "email": email, "telefone": telefone, "bio": bio}

            # atualizar
            resposta = self.controller.atualizar(autor_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Autor atualizado com sucesso."
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
        self.console.rule(title="Listagem de Autores", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
            for autor in resposta["message"]:
                message += f"\n{str(autor[0]).rjust(2)}" + f" | {autor[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do autor para excluir: ")
            autor_info = {"id": id}

            # atualizar
            resposta = self.controller.excluir(autor_info)
            if resposta["success"]:
                message = f"\n[green]Autor excluído com sucesso."
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
        self.console.rule(title="Listagem de Autores", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}"
            for autor in resposta["message"]:
                message += f"\n{str(autor[0]).rjust(2)}" + f" | {autor[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id do autor para listar: ")
            autor_info = {"id": id}

            # atualizar
            resposta = self.controller.listar_por_id(autor_info)
            if resposta["success"]:
                message = f"Id: {resposta["message"][0]}\n"
                message += f"Nome: {resposta["message"][1]}\n"
                message += f"Email: {resposta["message"][2]}\n"
                message += f"Telefone: {resposta["message"][3]}\n"
                message += f"Bio: {resposta["message"][4]}"
            else:
                message = f"[red]Erro: {resposta["error"]}."

            self.console.clear()
            self.console.rule(title="Listagem de Autores", align="center")
            self.console.print(f"{message}")
            self.console.rule(align="center")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar.")
