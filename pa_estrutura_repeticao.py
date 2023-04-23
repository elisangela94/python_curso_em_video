#Progeressão aritmética
print('---------------------')
print('10 TRMOS DE UMA PA')
print('---------------------')
primeiro = int(input('Digite o primeiro termo da progressão aritmética que deseja:'))
razao = int(input('Qual a razão:'))
decimo = primeiro + (10-1) * razao


for c in range (primeiro,decimo, razao):
        print(c)
print("Acabou")

