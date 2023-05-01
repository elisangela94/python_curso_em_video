# Faça um jogo que joque par pu ímpar com o computador 

from random import randint

print('jogo de par ou ímpar')
count = 0
while True:
    num = int(input('Escolha um número:'))
    computador = randint(1, 10)
    escolha = ' '
    while escolha not in "PI":
        escolha = str(input('Par ou Ímpa[P/I]:')).upper()
    if (num+computador)%2 == 0:
        if escolha == 'P':
            print(f'Você jogou o número {num} e o computador {computador}. Total de {num+computador}, deu par')
            print('Você venceu!!!')
        elif escolha == 'I':
            break
    elif (num+computador)%2 != 0:
        if escolha == 'I':
            print(f'Você jogou o número {num} e o computador {computador}. Total de {num+computador}, deu ímpa')
            print('Você venceu!!!')
        elif escolha == 'P':
            break
        count += 1
        print('Vamos jogar novamente...')
print(f'Você jogou o número {num} e o computador {computador}. Total de {num+computador},', end= '')
print('deu ímpa' if escolha == 'P' else 'deu par')
print('Perdeu')
print(f'Game over! voce acertou {count} vezes')
