import math
num = float(input('Qual o comprimento do cateto oposto(cm): '))
num2 = float(input('Qual o comprimeto do cateto adjacente(cm): '))
co = num**2
ca = num2**2
h = math.sqrt(co+ca)
print('O comprimento da hipotenusa é: {:.2f} cm'.format(h))