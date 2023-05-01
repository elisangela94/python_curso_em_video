# Tabuada de vários números
# será interropido quando o número for negativo

valor = 0
while True:
    valor = 0
    n = 1
    valor = int(input('Quer ver a tabuada de qual valor:'))
    if valor < 0:
        break
    while n < 11:
        print(f'{n} x {valor} = {n*valor}')
        n += 1
    print('-'*30)

print('Fim')

