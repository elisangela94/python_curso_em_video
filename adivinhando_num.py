#sortei um número entre 0 e 10 e peça para o usuário descobrir qual foi o número escolhido pelo Pc
#mostrando no final quantos palpites foram necessário para vencer 
from random import randint
import random
from time import sleep
n = randint(0, 10)
print('Adivinhe, qual o número entre 0 e 10 foi o selecionado!')
count = 0
acertou = False 
while not acertou :
    jogador = int(input('Qual o seu palpite?'))
    count += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('mais.. tente mais uma vez.')
        elif jogador > n:
            print('menos.. tente mais uma vez')
print('Parabéns! você conseguiu adivinhar o número e foram necessárias {} tentativas.'.format(count))