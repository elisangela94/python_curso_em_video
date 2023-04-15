salario = float(input('Qual seu sslário:'))
x = salario*0.1
y = salario*0.15
if salario >= 1250:
    print('O valor do seu aumemto será {} R$'.format(x))
else:
    print('O valor do seu aumento será {} RS'.format(y))