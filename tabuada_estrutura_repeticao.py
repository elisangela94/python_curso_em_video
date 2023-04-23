# tabuada que o usuario escolher, utilizando o laço for
from time import sleep
n1 = int(input("Digite o número da tabuada desejada:"))
print('A tabuada de {} é:'.format(n1))
sleep(2)

for c in range (1,11):
    print ("{} x {} = {}".format(c, n1, c*n1))