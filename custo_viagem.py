#calcule o preço da viagem
distancia = float(input('Qual distancia pecorrida em Km?'))
if distancia <= 200:
    print('o preço da passagem será {} R$'.format(distancia*0.5))
else:
    print('O preço da passagem custará {} R$'.format(distancia*0.45))