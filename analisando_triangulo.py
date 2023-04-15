print('alavie se os comprimentos são adequados para formar um triângulo')
R1 = float(input('Digite o comprimento da primeira reta:'))
R2 = float(input('Digite o comprimento da segunda reta:'))
R3 = float(input('Digite o comprimento da primeira reta:'))

if (R1+R2)>R3 and (R2+R3)>R1 and (R1+R3)>R2:
    print('De acordeo com as medidas, é possivel formar um triângulo!')
else:
    print('Não é possivel formar um triângulo')