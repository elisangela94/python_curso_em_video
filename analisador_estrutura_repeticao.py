# ler nome, idade e sexo de quatro pessoas
# mostrar a média da idade do grupo, nome do homem mais velho
#Quantas mulheres tem menos de 20 anos 
soma_idade = 0
#mediaidade = 0
maior_idade_homem = 0
nome_velho = ''
feminino = 0
masculino = 0
mulher20 = 0
print('Informações coletadas de 4 pessoas aleatórias!')
for p in range(1,5):
    print('----- {}º pessoa -----'.format(p))
    nome = str(input('Qual seu nomme:'))
    idade = int(input('Qual sua idade: '))
    soma_idade += idade
    print('Qual seu sexo? EScolha: \n [1] Feminino \n[2] Masculino')
    sexo = int(input('Escolha uma das opções:'))
    if p ==1 and sexo == 2:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 2 and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 1 and idade < 20:
        mulher20 += 1

mediaidade = soma_idade/4
print('A média de idade do grupo é: {}'.format(mediaidade))
print('O mais velho tem {}anos, e se chama {}.'.format(maior_idade_homem,nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))
