# Ler idade e sexo de várias pessoas
# No final perguntar se o usuário quer continuar ou não
# Quantas tem mais de 18 anos, quantas são homens e quantas mulheres tem menos de 20


maior = homem = mulher20 = 0
sexo = ""
continuar = ''
while True:
    print('Cadastro de pessoas')
    idade = int(input('Qual é sua idade:'))
    sexo = str(input('Qual seu sexo [F/M]:')).upper()
    while sexo != "M" and sexo != "F":
        if sexo != "M" and sexo != "F":
            print('Digite novamente, só é aceito como resposta M ou F')
        sexo = str(input('Qual seu sexo [F/M]:')).upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = str(input('Deseja continuar[S/N]:')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar[S/N]:')).upper()
    if continuar == 'N':
        break
print('O total de pessoas maior de 18 anos foi {}'.format(maior))
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
