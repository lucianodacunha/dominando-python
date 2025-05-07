"""
1. Criar três variáveis: nome (texto), idade (número) e altura (número decimal) 
capturadas pelo input(). Depois, imprimir essas informações formatadas.
2. Solicitar dois números, exibir a soma, subtração, multiplicação e divisão 
entre eles. (Não é necessário tratar erros por enquanto)
3. Solicitar um número para exibir o dobro, o triplo e a raiz quadrada dele.
4. Solicitar dois números e mostrar a média aritmética entre eles.
5. Solicitar a quantidade de quilômetros percorridos e o tempo gasto em minutos
(distância / tempo).
"""

#1 
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}")

#2 

num1 = int(input("\nInforme o primeiro número inteiro: "))
num2 = int(input("Informe o primeiro número inteiro: "))

print(f"Soma: {num1} + {num2} = {num1 + num2}")
print(f"Subtração: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
print(f"Divisão: {num1} / {num2} = {num1 / num2}")

#3 

from math import sqrt

num3 = int(input("\nInforme um número: "))

print(f"O dobro de {num3} é {num3 * 2}")
print(f"O triplo de {num3} é {num3 * 3}")
print(f"A raiz quadrada de {num3} é {sqrt(num3)}")

#4 

num4 = int(input("\nEntre com um número: "))
num5 = int(input("Entre com outro número: "))
media = (num4 + num5) / 2

print(f"A média aritmética entre {num4} e {num5} é {media}")

#5

kilometros = float(input("\nEntre com a distância percorrida (km): "))
minutos = float(input("Entre com o tempo gasto (minutos): "))

horas = minutos / 60
velocidade = kilometros / horas

print(f"A velocidade média é de {velocidade}")