# exercise 90
# Criete a program that reads the name and media, informing the situation of the student
# saving everything in a dictionary, at the and show the content of the structure on the screen

dici = dict()
test = list()
situation = " "


name = input(str("Qual o nome do aluno (a): "))
media = float(input("Qual a media:"))
test.append(name)
test.append(media)

if media >= 7:
    situation = "APROVADO"
else:
    situation = "REPROVADO"
test.append(situation)
dici["SITUAÇÃO"] = test
print(dici)
