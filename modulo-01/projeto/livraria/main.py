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
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def biografia(self) -> str:
        return self._biografia

    @biografia.setter
    def biografia(self, biografia: str) -> None:
        self._biografia = biografia
    
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


#====Categoria====#
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


#====Editora====#
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


#====Autor====#
def menu_autores() -> None:
    while True:
        console.clear()
        console.rule(title="Menu Autores", align="center")
        console.print("1 - Listar\n" +
                      "2 - Cadastrar\n" +
                      "3 - Excluir\n" + 
                      "4 - Editar\n" + 
                      "5 - Listar por Id\n" +
                      "6 - Voltar")
        console.rule(align="center")    
        opcao = console.input("\nInforme a opção desejada: ")
        match opcao:
            case "1":
                listar_autores()
            case "2":
                cadastrar_autores()
            case "3":
                excluir_autores()
            case "4":
                editar_autor()            
            case "5":
                listar_autor_por_id()
            case "6":
                break
            case _:
                console.input("\n[red]Opção inválida. Pressione enter para " + 
                                "continuar... ")


def listar_autores() -> None:
        console.clear()
        console.rule(title="Listagem de Autores", align="center")
        if autores:
            console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
            for autor in autores:
                console.print(f"{str(autor.id).rjust(2)}" + 
                            f" | {autor.nome.ljust(30)}")
        else:
            console.print("[red]Nenhum autor cadastrado.")
        console.rule(align="center")    
        console.input("\nPressione enter para continuar...")


def excluir_autores() -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + 
                        f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center") 

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break
    autor = autores.pop(idx)
    console.input(f"\nAutor {autor.nome} removido com sucesso." + \
                  f"\nPresione enter para continuar...")


def listar_autor_por_id() -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + 
                        f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")     

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break

    autor = autores[idx]
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    console.print(f"Id: {autor.id}\n" + \
                  f"Nome: {autor.nome}\n" + \
                  f"Biografia: {autor.biografia}")
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


def editar_autor() -> None:
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    if autores:
        console.print(f"{'Id'.rjust(2)} | {'Nome do Autor'.ljust(30)}")
        for autor in autores:
            console.print(f"{str(autor.id).rjust(2)}" + 
                        f" | {autor.nome.ljust(30)}")
    else:
        console.print("[red]Nenhum autor cadastrado.")
    console.rule(align="center")     

    id = int(console.input("Entre com o id do autores para excluir: "))
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break

    autor = autores[idx]
    console.clear()
    console.rule(title="Listagem de Autores", align="center")
    nome = console.input("\nInforme o nome do autor: ")
    bio = console.input("Informe a biografia do autor: ")
    autor.nome = nome
    autor.biografia = bio    
    console.rule(align="center")
    console.input(f"\nAutor {autor.nome} editado com sucesso. " + \
                  f"\nPressione enter para continuar...")
    

#====Livro====#
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
