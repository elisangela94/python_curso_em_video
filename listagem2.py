#P rograma que leia 4 valores e guarde-os em uma tupla
# Depois a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o valor 3
# Quais foram os números pares

print('Digite 4 valores inteiros')
numero = []
pares = []
tres = 0
for c in range(0,4):
    num = int(input('Digite um número: '))
    for n in range(4):
        numero.append(num)
    if (num%2) == 0:
        pares.append(num)
    if num == 3:
        tres += 1

tupla = tuple(numero)

print(f'O número 9 apareceu: {tupla.count(9)} ')
if tres == 0:
    print('O número três não apareceu nenhuma vez')
else:
    print(f'O número 3 apareceu na posição {tupla.index(3)+ 1} ')
print(f'Os números pares são: {pares}')
