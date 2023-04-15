#sorteio entre alunos 
import random
n1 = str(input("primeiro aluno: "))
n2 = str(input("segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quearto aluno: "))
mylist = [n1, n2, n3, n4]
random.shuffle(mylist)
firstElement = mylist[0]
print("A ordem de sequência escolhida é {}\n  e o aluno escolhido é {}".format(mylist, firstElement) )


