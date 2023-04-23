#contagem regressiva para fogos de artificio de 10 a 0
#Pausa de um segundo entre eles 
from time import sleep

print('Contagem regressiva!')
for contagem in range (10,-1,-1):
    print(contagem)
    sleep(1)
print("Feliz ano novo! ")

