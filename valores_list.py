# Criar lista com valores numéricos e unicos e exibir em ordem crescente
# Exercicio 79

valores = list()
resp = "S"
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Não é permitido valor duplicado ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper()
    if resp in 'Nn':
        break

valores.sort()

print(f'Os valores acrecentados a lista formam: {valores}')