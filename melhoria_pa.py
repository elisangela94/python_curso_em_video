#Progeressão aritmética com a função while
# Perguntando se quer continuar
# Encerra quando digitar N
print('---------------------')
print('10 TRMOS DE UMA PA')
print('---------------------')
primeiro = int(input('Digite o primeiro termo da progressão aritmética que deseja:'))
razao = int(input('Qual a razão:'))
decimo = 0
pa = ""
print(primeiro)
while decimo < 9:
    primeiro += razao
    decimo += 1
    print(primeiro)
p = str(input('Deseja dar coninuação nos termos acima? S/N:')).upper()
while p == "S":
    termo = int(input('Quantos termos á mais você deseja: '))
    newTermo = decimo + termo
    while newTermo > decimo:
        primeiro += razao
        decimo += 1
        print(primeiro)
    p = str(input('Deseja dar coninuação nos termos acima? S/N:')).upper()
print('Acabou')
