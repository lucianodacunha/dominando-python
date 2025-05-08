
def ex_01() -> str:
    """Solicitar dois números ao usuário e calcular a soma, subtração, 
    multiplicação, divisão inteira e resto."""

    msge: str = ""
    num1 = int(input("\nInforme o primeiro número inteiro: "))
    num2 = int(input("Informe o primeiro número inteiro: "))

    msge += f"Soma: {num1} + {num2} = {num1 + num2}"
    msge += f"\nSubtração: {num1} - {num2} = {num1 - num2}"
    msge += f"\nMultiplicação: {num1} * {num2} = {num1 * num2}"
    msge += f"\nDivisão: {num1} / {num2} = {num1 / num2}"
    msge += f"\nResto: {num1} % {num2} = {num1 % num2}"
    return msge

def ex_02() -> str:
    """Solicitar um número e mostrar se ele é divisível por 5 e 7, utilizando o
    operador %."""

    msge: str = ""
    num3 = int(input("\nInforme o primeiro número inteiro: "))
    msge = f"{num3} é divisível por {5}? {'Sim' if num3 % 5 == 0 else 'Não'}"
    msge += f"\n{num3} é divisível por {7}? {'Sim' if num3 % 7 == 0 else 'Não'}"
    return msge


def ex_03() -> str:
    """Criar uma função que receba um número e retorne se ele é positivo, 
    negativo ou zero."""

    msge: str = None
    num4 = int(input("\nInforme o primeiro número inteiro: "))
    if num4 > 0:
        msge = f"O número {num4} é positivo."
    elif num4 < 0:
        msge = f"O número {num4} é negativo."
    else:
        msge = f"O número {num4} é igual a 0."
    return msge

def ex_04() -> str:
    """Solicitar dois números e verificar se o primeiro é maior que o segundo 
    e se a soma deles é maior que 100."""

    msge: str = ""

    num5 = int(input("\nInforme o primeiro número inteiro: "))
    num6 = int(input("Informe o primeiro número inteiro: "))
    soma = num5 + num6

    msge = f"{num5} é > {num6}" if num5 > num6 else f"{num6} é > {num5}"
    msge += f"\n{num5} + {num6} é > 100" if soma > 100 else f"\n{num6} + {num5} não é > 100"
    return msge

def ex_05() -> str:
    """ Criar um programa que utilize o match case para determinar a estação do
     ano com base no número do mês (1 a 12)."""

    estacao: str = ""

    while True:
        mes = int(input("\nInforme o mês atual: "))
        match mes:
            case 1 | 2 | 3:
                estacao = f"Mês {mes}: Você está no VERÃO"
                break            
            case 4 | 5 | 6:
                estacao = f"Mês {mes}: Você está no OUTONO"
                break
            case 7 | 8 | 9:
                estacao = f"Mês {mes}: Você está no INVERNO"
                break
            case 10 | 11 | 12:
                estacao = f"Mês {mes}: Você está na PRIMAVERA"
                break
            case _:
                input(f"\nOpção inválida. Pressione enter para continuar...")
    return estacao


print(ex_01())
print(ex_02())
print(ex_03())
print(ex_04())
print(ex_05())