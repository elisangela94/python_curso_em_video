# Tupla com nomes de produtos e seus respectivos preços na sequencia
# No final, mostre uma listagem de preços. Organizando os daods em forma tabular
lista_tupla = ('Lápis', 1.75,
                'Borracha', 2.00,
                'Caderno', 15.90,
                'Estojo', 25.00,
                'Compasso', 9.99,
                'Mochila', 120.32,
                'Canetas', 22.30)
print('-=' *30)
print(f'{"Tabela de preços":^40}') #'^' utilizado para centralizar
print('-=' *30)

for posicao in range(0, len(lista_tupla)):
    if posicao % 2 == 0:
        print(f'{lista_tupla[posicao]:.<30}', end= '') #.<30, para alinhar a esquerda(<) e preencher com pontos o espaço restante
    else:
        print(f'R${lista_tupla[posicao]:>7.2f}') #.2f (duas casas decimais)