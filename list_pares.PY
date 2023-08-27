# EXERCICIO 85
# USUÁRIO IRÁ DIGITAR 7 VALORES NUMÉRICOS, CADASTRANDO - OS EM UMA UNICA LISTA
# MANTENDO SEPARADOS OS VALORES PARES E ÍMPARES, MOSTRE OS VALORES EM ORDEM CRESCENTE

num = [[], []]
value = 0 

for r in range(1,8):
    value = int(input(f'Digite o {r}º valor:'))
    if value%2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)
num[0].sort()
num[1].sort()
print(f'Os valores são: {num[0]}')
print(f'Os valores ímpares são: {num[1]}')
