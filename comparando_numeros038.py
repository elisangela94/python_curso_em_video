#ler dois números inteiros e comparalos 
print('Comparando os núumeros')
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))

if n1>n2:
    print('O primeiro valor é maior!')
elif n2>n1:
    print('O segundo valor é maior!')
else:
    print('Os dois valores são iguais!')