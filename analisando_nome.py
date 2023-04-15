nome = str(input('Digite seu nome: ')).upper().strip()
FatiaN = nome.split()
print('Seu primeiro nome é {}'.format(FatiaN[0]))
print('Seu último nome é {}'.format(FatiaN[len(FatiaN)-1]))