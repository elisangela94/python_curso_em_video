# Crie uma tupla, com uma contagem por extenso de 0 a 20 
#o programa terá que ler o número pelo teclado e mostra-lo por extenso 

n = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    num = int(input('Digite um número entre 0 até 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')

numero_extenso = n[num]
print(f'O número {num} por extenso é: {numero_extenso}')