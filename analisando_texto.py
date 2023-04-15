#leia o nome completo de uma pessoa
#O nome com todas as letras maiusculas
#Com todos minusculos
#quanmtas letras sem consideras espaços
#Quantas letras tem o primeiro nome

nome = input('Nome: ')
nomeSemEspaço = nome.replace(" ", "")
P = nome.split()# Divide a frase em palavras
primeiroP = P[0]


print(nome.upper())
print(nome.lower())
print(len( nomeSemEspaço))
print(len(primeiroP))