# calculando o IMC
peso = float(input('Qual é seu peso? (kg): '))
altura = float(input(' Qual é sua altura? (m): '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é {:.1f} '.format(imc))

if imc < 18.5:
    print('você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('você está no peso ideal!')
elif 25 <= imc < 30:
    print('você está em sobrepeso!')
elif 30 <= imc < 40:
    print("cuidado! Você esta em obesidade.") 
else:
    print('Cuidado! Você esta em obesidade mórbida.')