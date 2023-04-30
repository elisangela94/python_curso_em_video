#Leia varios números inteiros 
#vai parar quando digitar o número 999
p = 0
x = 0
count = 0
while p != 999:
    p = int(input('Digite um número:'))
    if p != 999:
        x += p
    count += 1
print("Foi digitado {} vezes, e o valor total é {}".format(count-1, x))