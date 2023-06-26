# Criar lista (exercicio 81)
# No final, dizer quantos números foram digitados
# Ordenar em forma decresente
# e dizer se o número 5 foi digitado

valores = list()
resp = "S"
count = 0
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Não é permitido valor duplicado ')
    count += 1
    resp = str(input('Deseja continuar?[S/N]: ')).upper()
    if resp in 'Nn':
        break

valores.sort(reverse=True)
print(f'Foram digitados {count} números')
print(f'Os valores em ordem decrescente são: {valores}')