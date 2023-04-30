# Faça um programa que leia um número e diga seu fatorial
print('Calculando o fatorial')
n1 = int(input('Digite um número: '))
i = n1
resultado = 1
print('O fatorial de {}! = '.format(n1), end='')
while i > 0: 
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end= '')
    resultado *= i
    i -= 1 
print('{}'.format(resultado), end='\n')