n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o último nmúmero: '))

if n1>n2 and n1>n3:
    print('O maior número é {:.2f}'.format(n1))
if n2>n1 and n2>n3: 
    print('O maior número é {:.2f}'.format(n2))
else:
    print('O maior número é {:.2f}'.format(n3))

if n1<n2 and n1<n3:
    print('O menor número é {:.2f}'.format(n1))
if n2<n1 and n2<n3: 
    print('O menor número é {:.2f}'.format(n2))
else:
    print('O menor número é {:.2f}'.format(n3))