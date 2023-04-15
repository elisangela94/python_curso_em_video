#sortei um número entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo Pc
import random
from time import sleep
n = [0, 1, 2, 3, 4, 5]
random.shuffle(n)
firstnum = n[0]
num = int(input('Adivinhe, qual o número entre 0 e 5 foi o selecionado?'))
print('Processando...')
sleep(3)
if num == firstnum:
   print("você acertou, parabéns!")
else:
  print('número incorreto, o valor selecionado foi {}'.format(firstnum))