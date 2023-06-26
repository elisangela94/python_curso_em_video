# Exercicio 80
# Sem usar a função append

valores = list()
resp = "S"
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.insert(num, num)
    else:
        print('Não é permitido valor duplicado ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper()
    if resp in 'Nn':
        break

valores.sort()

print(f'Os valores acrecentados a lista formam: {valores}')