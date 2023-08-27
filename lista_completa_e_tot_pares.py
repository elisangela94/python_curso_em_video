# Criar lista (exercicio 82)
# No final, dizer separar uma lista com todos, outra com num pares e outra com num ímpares

valores = list()
pares = list()
impar = list()
resp = 'S'

while True:
    num = int(input('Digite um número:'))
    if num not in valores:
        valores.append(num)
    else:
        print('Não é permitido valores duplicados.')
    if num%2 == 0:
        pares.append(num)
    if num%2 != 0:
        impar.append(num)

    resp = str(input('Deseja continuar?[S/N]: ')).upper()
    if resp in 'Nn':
        break

print(f'A lista completa é: {valores}')
print(f'Os valores pares digitados são: {pares}')
print(f'Os valores ímpares são: {impar}')