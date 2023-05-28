# Crie um programa que gere 5 números aleatórios e coloque-os em uma tupla
# Depois disso mostre a listagem de números gerados, mostrando também o menor e maior valor.

import random

numeros = []
for c in range(5):
    numeros.append(random.randint(0, 1000))

numeros_tupla = tuple(numeros)
print(f'Os 5 números aleatórios são: {numeros_tupla}')

menor_valor = min(numeros_tupla)
maior_valor = max(numeros_tupla)
print(f'O menor valor é: {menor_valor}')
print(f'O maior valor é: {maior_valor}')
