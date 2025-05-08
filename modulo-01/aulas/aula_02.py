"""
A partir dos valores da base e altura de um triângulo, calcular e exibir sua 
área.
Fórmula: (base * altura) / 2.
"""

# base = float(input("Informe o valor da base do triângulo: "))
# altura = float(input("Informe o valor da altura do triângulo: "))
# area = (base * altura) / 2

# print(f"Área do tringulo: {area:.2f}.")

"""
Armazenar dez números em uma lista. Exibir os valores na ordem inversa à da
digitação.
"""

# Método 1
lista = list(range(1, 11))
for i in lista:
    print(lista[len(lista) - i], end=" ")

print()

# Método 2
lista.reverse()
for i in lista:
    print(i, end=" ")

print()
