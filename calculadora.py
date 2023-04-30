# Ler dois números e mostre menu na tela
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
resposta = 0
while resposta != 5:
    print(' [1] Somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
    resposta = int(input('Escolha uma das opções:'))
    if resposta == 1:
        print('A soma dos dois número é {}'.format(n1+n2))
    elif resposta == 2:
        print('A multiplicação entre os dois números ś {}'.format(n1*n2))
    elif resposta == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {} '.format(n2))
    elif resposta == 4:
        print('Informe os números novamente')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif resposta == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente..')
print("Fim, volte sempre!")