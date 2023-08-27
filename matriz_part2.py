# exercicio 87
# além de criar uma matriz, mostrar a soma dos valores pares, a soma dos valores da terceira coluna 
# e o maior da segunda linha 
tot_par = third_column = bigger_s = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o número para a posição{[l], [c]}:'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= '') # :^5 = centraliza 
        if matriz[l][c] % 2 == 0:
            tot_par += matriz[l][c]
    print()
for l in range(0,3):
    third_column += matriz[l][2]
for l in range(0,3):
    if c == 0:
        bigger_s += matriz[1][c]
    elif matriz[1][c] > bigger_s:
        bigger_s = matriz[1][c]
print('-=' *30)
print(f'A soma dos valores pares é: {tot_par}')
print(f'A soma da terceira coluna é: {third_column}')
print(f'O maior valor da segunda linha é:{bigger_s}')