#Programa para aprovar um empréstimo 
#valor da casa
#em quantos anos pretende pagar 
#valor não pode exceder 30% do salario
valor = float(input('Qual o valor da casa que você deseja financiar?'))
salario = float(input('Qual valor do seu salário?'))
ano = int(input('Em quantos anos pretende pagar'))
medida = valor/(ano*12)
if (salario*0.3) < medida:
    print('Infelizmente seu empréstimo foi negado, não permitimos que seu salário exceda 30% das parcelas programadas')
else:
    print('parabéns, seu empréstimo foi aprovado! Suas parcelas serão de {:.2f} por mês'.format(medida))

