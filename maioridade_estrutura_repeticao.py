#leia o ano de nascimento de 7 pessoas
#No final mostre quantas são maiores de idade e quantas não são.

anos = []
maior = 0
menor = 0
for c in range (1,8):
    n1 = int(input('Qual seu ano de nascimento:'))
    anos.append(n1)
    if (2023-n1) <21:
        menor += 1
    else:
        maior += 1
#for nascimento in anos:
print('Os anos digitados foram: {}'.format(anos))
print('Foi analisado que há {} pessoas maiores de idade'.format(maior))
print('Foi analisado que há {} pessoas menores de idade'.format(menor))

