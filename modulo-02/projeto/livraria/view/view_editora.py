from rich.console import Console
from controller.controller_editora import EditoraController


class EditoraView:
    def __init__(self):
        self.console = Console()
        self.controller = EditoraController()


    def menu(self) -> None:
        while True:
            self.console.clear()
            self.console.rule(title="Menu Editoras", align="center")
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
        self.console.rule(title="Cadastro de Editoras", align="center")
        nome = self.console.input("Informe o nome do editora: ")
        endereco = self.console.input("Informe o endereco do editora: ")
        telefone = self.console.input("Informe o telefone do editora: ")
        editora_info = {"nome": nome, "endereco": endereco, "telefone": telefone}
        self.console.rule(align="center")

        resposta = self.controller.inserir(editora_info)
        if resposta["success"]:
            message += f"\n[green]{resposta["message"]}."
        else:
            message += f"\n[red]Falha ao inserir editora "
            message += f"\n{resposta["error"]}."

        self.console.input(f"{message}\nPressione enter para continuar...")


    def listar(self) -> None:
        message: str = ""
        resposta = self.controller.listar()

        self.console.clear()
        self.console.rule(title="Listagem de Editoras", align="center")

        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
            for editora in resposta["message"]:
                message += f"\n{str(editora[0]).rjust(2)}" + f" | {editora[1].ljust(30)}"
        else:
            message += f"[red]{resposta["error"]}"

        self.console.print(f"{message}")
        self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar...")


    def atualizar(self) -> None:
        message: str = ""

        self.console.clear()
        self.console.rule(title="Listagem de Editoras", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
            for editora in resposta["message"]:
                message += f"\n{str(editora[0]).rjust(2)}" + f" | {editora[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id da editora para editar: ")
            nome = self.console.input("Informe o nome da editora: ")
            endereco = self.console.input("Informe o endereco da editora: ")
            telefone = self.console.input("Informe o telefone da editora: ")
            editora_info = {"id": id, "nome": nome, "endereco": endereco, "telefone": telefone}

            # atualizar
            resposta = self.controller.atualizar(editora_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Editora atualizada com sucesso."
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
        self.console.rule(title="Listagem de Editoras", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
            for editora in resposta["message"]:
                message += f"\n{str(editora[0]).rjust(2)}" + f" | {editora[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id da editora para excluir: ")
            editora_info = {"id": id}

            # atualizar
            resposta = self.controller.excluir(editora_info)
            if resposta["success"]:
                message = (
                    f"\n[green]Editora excluída com sucesso."
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
        self.console.rule(title="Listagem de Editoras", align="center")

        # listar
        resposta = self.controller.listar()
        if resposta["success"]:
            message += f"{'Id'.rjust(2)} | {'Nome da Editora'.ljust(30)}"
            for editora in resposta["message"]:
                message += f"\n{str(editora[0]).rjust(2)}" + f" | {editora[1].ljust(30)}"

            self.console.print(f"{message}")
            self.console.rule(align="center")

            id = self.console.input("\nEntre com o id da editora para listar: ")
            editora_info = {"id": id}

            # atualizar
            resposta = self.controller.listar_por_id(editora_info)
            if resposta["success"]:
                message = f"Id: {resposta["message"][0]}\n"
                message += f"Nome: {resposta["message"][1]}\n"
                message += f"Endereco: {resposta["message"][2]}\n"
                message += f"Telefone: {resposta["message"][3]}"
            else:
                message = f"[red]Erro: {resposta["error"]}."

            self.console.clear()
            self.console.rule(title="Listagem de Editoras", align="center")
            self.console.print(f"{message}")
            self.console.rule(align="center")
        else:
            message += f"[red]{resposta["error"]}"
            self.console.print(f"{message}")
            self.console.rule(align="center")
        self.console.input(f"\nPressione enter para continuar.")
