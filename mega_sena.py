# exercicio 88
# Pergunte ao usuário quantos jogos da mega sena ele quer e mostre na tela
from random import randint
from time import sleep
print('-' *20)
print('     MEGA SENA     ')
print('-' *20)
tot_list = list()

tot_jogos = int(input('Quantos jogos você quer?'))
for c in range(1,tot_jogos + 1):
    print(f'Jogo {c}', end= ' ')
    value = []
    for j in range(0,6):
        n = randint(1,60)
        if n not in value:
            value.append(n)
    value.sort()
    print(f'{value}')
    value.clear
    sleep(1)
print('-' *20)
print('     BOA SORTE     ')
print('-' *20)

