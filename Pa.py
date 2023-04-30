#Progeressão aritmética com a função while
print('---------------------')
print('10 TRMOS DE UMA PA')
print('---------------------')
primeiro = int(input('Digite o primeiro termo da progressão aritmética que deseja:'))
razao = int(input('Qual a razão:'))
#decimo = primeiro + (10-1) * razao
decimo = 0
pa = ""
print(primeiro)
while decimo < 9:
    primeiro += razao
    decimo += 1
    print(primeiro)
print("Acabou")