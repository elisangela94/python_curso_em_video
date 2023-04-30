#leia um número inteiro e mostre na tela os n primeiros elementos da sequencia 

perg = int(input('Digite a quantidade de termos da sequência de fibonacci você deseja:'))
c = 0
p = [0, 1]
while c < perg-2:
    p.append(p[c] + p[c+1]) 
    c+=1
print(p)