velocidade = float(input('Qual a velocidade do carro:'))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Seu carro foi multado, a multa será de {:.2f} R$'.format(multa))
else:
    print('Parabéns, seu carro esta no limite permitido')