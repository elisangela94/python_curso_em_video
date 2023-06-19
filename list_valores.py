# Ler 5 números e por em uma lista
# mostrar qual é o maior e qual é o menor

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))

print (f'Os valores escolhidos foram: {valores}')
print(f'O maior valor digitado é: {max(valores)}')
print(f'O menor valor digitado é: {min(valores)}')