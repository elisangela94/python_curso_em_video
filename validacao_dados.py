#ler o sexo de uma pessoa mas só aceita "M" ou "F"
# Mas Se caso estiver errado pedir p digitar novamente

sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input('Digite qual seu sexo:')).upper()
    sexo = sexo
    if sexo != "M" and sexo != "F":
        print('Digite novamente, só é aceito como resposta M ou F')
print('Sexo {} registrado com sucesso'.format(sexo))