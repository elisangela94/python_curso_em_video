#conversão para binario, octal e hexadecimal
n = int(input('Digite um numero que deseja converter:'))
print('Escolha uma das bases para conversão:')
print('[1] converter para binário.')
print('[2] converter para octal.')
print('[3] converter para hexadecimal')
opcao = int(input('Escolha sua opção:'))
if opcao == 1:
    print('{} convertido para binario é igual a {} '.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {} '.format(n,oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {} '.format(n, hex(n)[2:]))
else:
    print('Opção inválida. tente novamente!')