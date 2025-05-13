def ex_01() -> str:
    """Crie um programa que irá solicitar o nome de 4 cidades que você gostaria
    de conhecer. Depois imprima uma frase no seguinte formato:
    Eu gostaria de visitar estas cidades: Amsterdam, Wellington, Machu Picchu,
    Santiago."""

    cidades: set[str] = set()

    while len(cidades) < 4:
        cidades.add(input("Entre com o nome de uma cidade que deseja visitar: "))

    return f"Eu gostaria de visitar as seguintes cidades: {' '.join(list(cidades))}"


def ex_02() -> str:
    """Tendo um CPF dentro de uma string no formato '12345678900', desenvolva
    um programa para imprimir esse CPF no formato: '123.456.789-00'"""

    cpf = "12345678900".rjust(11, "0")
    return f"CPF formatado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def ex_03() -> str:
    """Entrar via teclado com um valor positivo qualquer.
    Validar se o usuário está digitando um valor positivo.
    Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um
    a dez."""

    msge: str = ""
    valor = int(input("Entre com um valor: "))

    while valor < 1:
        valor = int(input("Enter com um valor positivo!: "))

    for _, operador in enumerate(range(11)):
        msge += f"{valor} X {operador} = {valor * operador}\n"

    return msge


def ex_04() -> str:
    """Armazenar dez números (usando entrada de dados - input) em uma lista.
    Após a digitação dos valores, criar uma rotina para ler os valores e achar
    e exibir o maior deles."""

    lista = list()

    for i in range(10):
        lista.append(int(input("Entre com um número: ")))

    return f"Maior número da lista: {max(lista)}"


def ex_05() -> str:
    """Crie um programa para sanitizar uma lista contendo vários tipos de
    objetos. A sanitização se dará através da remoção de strings vazias."""

    lista = ["", -1, 3.14, "Python", 3j + 35, "", None, Exception(), 42, True, ""]

    return ", ".join(map(str, filter(lambda x: x != "", lista)))


def ex_06() -> str:
    """Armazenar 5 números (usando entrada de dados) em uma lista.
    Após a digitação, solicitar uma constante numérica que deverá alterar cada
    elemento da lista através da multiplicação entre a constante e o próprio
    elemento."""

    numeros: list[int] = list()
    resultado: list[int] = list()
    constante: int = 0
    quantidade = 5

    for i in range(quantidade, 0, -1):
        numeros.append(int(input(f"Entre com um número (Faltam {i}): ")))

    constante = int(input("Entre com uma constante numérica: "))
    resultado = list(map(lambda x: x * constante, numeros))
    return f"Resultado: {', '.join(map(str, resultado))}"


def ex_07() -> str:
    """Dadas essas duas listas:
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    Crie um programa para alterar a list1 de forma a incorporar a sub_list para
    que o resultado seja este:
    ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    """

    list1: list[str] = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]

    list1[2][1][2].extend(sub_list)

    return f"[{', '.join(map(str, list1))}]"


def ex_08() -> str:
    """Um palíndromo é uma palavra ou frase que é escrita da mesma forma de
    trás para frente. Alguns exemplos são:
    "asa", "ama", "anotaram a data da maratona", "natan", "renner",
    "a cara rajada da jararaca"
    Escreva um programa para detectar se uma determinada string é um palíndromo
    ou não."""

    lista: list[str] = [
        "asa",
        "ama",
        "anotaram a data da maratona",
        "natan",
        "renner",
        "a cara rajada da jararaca",
    ]
    resultado: str = ""

    for p in lista:
        status = "é" if p.replace(" ", "") == p[::-1].replace(" ", "") else "não é"
        resultado += f"{p} {status} palindromo\n"

    return resultado


print(ex_01())
print(ex_02())
print(ex_03())
print(ex_04())
print(ex_05())
print(ex_06())
print(ex_07())
print(ex_08())
