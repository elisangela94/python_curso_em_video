#ler seis números inteiros 
#Somar apenas os numeros q pares
print('Digite 6 números:')
soma = 0

for c in range(0,3):
    numero = int(input('Qual numero deseja?'))
    if(numero%2) == 0:
        soma+= numero
    
print("A soma dos números pares digitados é: {}".format(soma))