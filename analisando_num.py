#ler vários números
#média entre todos eles 
#maior e menor valor lido
# o programa tem que perguntar se ele quer ou não continuar a digitar

print('Analisando números')
resposta = "S"
q = 0
tot = 0
maior = 0
menor = 0

while resposta == 'S':
    n1 = int(input('Digite um número: '))
    if q == 0:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    tot += n1
    q += 1
    resposta = str(input('Deseja continuar S/N:')).upper()
print('Você digitou {} números, a média foi: {}'.format(q, tot/q))
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))