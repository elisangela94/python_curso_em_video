# Crie uma tupla com varias vogais, depois disso, deve apresentar quais são as vogais presentes em cada palavra

palavras = ('Caderno', 'livro', 'celular', 'Geladeira', 'Carro', 'trabalhador', 'programador')
vogais = []

for posicao in palavras:
    print(f'\nNa palavra {posicao} temos', end= '')
    for letra in posicao:
        if letra.lower() in 'aieou':
            print(letra, end=' ')