#Soma entre todos os números impares que são multiplos de 3
# E que se encontram em um intervalo de 1 até 500

soma = 0
for c in range(1, 501):
    if (c%2) != 0 and (c%3) == 0:
        soma += c


print("A soma total é {}.".format(soma))
