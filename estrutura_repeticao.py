#dizer se é um numero primo
print('Descrubra se um número é número primo!')
numero = int(input('Digite um número: '))
quant = 0
# Um número é primo se for divisível apenas por 1 e por ele mesmo
# Então, verificamos se ele é divisível por algum número entre 2 e (n-1)
# Se ele for divisível por algum desses números, então ele não é primo

for c in range(1, numero + 1):
    if numero % c == 0:
        quant += 1

if quant == 2:
    print("Este número é um número primo")
else:
    print('Este número não é primo')
        

