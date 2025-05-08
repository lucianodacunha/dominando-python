from rich.console import Console
from rich.prompt import Prompt


console = Console()


class Autor:
    serial: int = 0

    def __init__(self, nome: str, biografia: str) -> None:
        self._id = Autor.get_id()
        self._nome = nome
        self._biografia = biografia

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def biografia(self) -> str:
        return self._biografia

    @classmethod
    def get_id(cls):
        Autor.serial += 1
        return Autor.serial
    
    def __str__(self) -> str:
        return f"{str(id).zfill(2)} - {self.nome}"


autores: list[Autor] = list()

def main() -> None:
  
    menu_principal()
    console.input("\n[red]Pressione enter para finalizar...")
    console.clear()


def menu_principal() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Principal", align="center")
        console.print("1 - Categorias\n" +
                      "2 - Editoras\n" +
                      "3 - Autores\n" + 
                      "4 - Livros\n" +
                      "5 - Sair")
        console.rule(align="center")   

        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                menu_categorias()
            case "2":
                menu_editoras()
            case "3":
                menu_autores()
            case "4":
                menu_livros()
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")     


def menu_categorias() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Categorias", align="center")
        console.print("1 - Listar\n" +
                      "2 - Cadastrar\n" +
                      "3 - Excluir\n" + 
                      "4 - Listar por Id\n" +
                      "5 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")


def menu_editoras() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Editoras", align="center")
        console.print("1 - Listar\n" +
                      "2 - Cadastrar\n" +
                      "3 - Excluir\n" + 
                      "4 - Listar por Id\n" +
                      "5 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")


def menu_autores() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
        console.print("1 - Listar\n" +
                      "2 - Cadastrar\n" +
                      "3 - Excluir\n" + 
                      "4 - Listar por Id\n" +
                      "5 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                listar_autores()
            case "2":
                cadastrar_autores()
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")


def listar_autores() -> None:
        console.clear()
        console.rule(title="Listagem de Autores", align="center")
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + 
                          f" | {autor.nome.ljust(30)}")
        console.rule(align="center")    
        console.input("\nPressione enter para continuar...")


def cadastrar_autores() -> None:
        console.clear()
        console.rule(title="Cadastro de Autores", align="center")
        nome = console.input("\nInforme o nome do autor: ")
        bio = console.input("Informe a biografia do autor: ")
        autor = Autor(nome=nome, biografia=bio)
        autores.append(autor)
        console.rule(align="center")    
        console.input("\nAutor cadastrado com sucesso. "
                      "Pressione enter para continuar...")

def menu_livros() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Livros", align="center")
        console.print("1 - Listar\n" +
                      "2 - Cadastrar\n" +
                      "3 - Excluir\n" + 
                      "4 - Listar por Id\n" +
                      "5 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")


if __name__ == "__main__":
    main()
