#leia o peso de 5 pessoas 
#mostrar qual foi o maior e menor peso
print('Digite os pesos de 5 pessoas:')
maior = 0
menor = 0
for p in range (1,6):
    n1 = float(input('Peso(kg):'))
    if p == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print('O maior peso digitado foi: {}'.format(maior))
print('O menor peso digitado foi: {}'.format(menor))


