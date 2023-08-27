# exercicio 84
# Com o nome e peso de varias pessoas 
# a) quantas foram registradas b) a lista com os mais pesados
# c) Uma lista com as pessoas mais leves 
temp = []
princ = []
menorp = maiorp = 0
count = 0
resp = 'S'
while resp == 'S':
    temp.append(str(input('Digite seu nome:')))
    temp.append(float(input('Qual seu peso:')))
    if len(princ) == 0:
        menorp = maiorp = temp[1]
    else:
        if temp[1] < menorp:
            menorp = temp[1]
        if temp[1] > maiorp:
            maiorp = temp[1]
    princ.append(temp[:]) # '[:]' serve pra fazer uma cópia dos valores temporarios para a lista principal
    temp.clear()

    resp = str(input('Deseja continuar?[S/N]:')).upper()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, foram cadastrados {len(princ)} pessoas')
print(f'O maior peso foi de {maiorp} kg. Peso de', end= ' ')
for p  in princ:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end= '')
print()
print(f'O menor peso foi de {menorp} kg. Peso de', end=' ')
for p in princ:
    if p[1] == menorp:
        print(f'[{p[0]}]', end =' ')