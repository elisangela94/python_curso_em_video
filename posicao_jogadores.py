# Tupla com os 20 primeiros da tabela do campeonato brasileiro de futebol 2022 na ordem de colocação 
# depois mostre: a) 5 primeiros b)utimos 4 colocados c) Na ordem d) em que posição está o Flamengo

posicao = ( 'Palmeiras SP', 'Internacional RS', 'Fluminense RJ', 'Corinthias SP', 'Flamengo RJ',
'Atletico Paranaense PR', 'Atlético Mineiro MG', 'Fortaleza CE', 'São Paulo SP', 'América MG',
'Botafogo RJ', 'Santos SP', 'Goiás GO', 'Bragantino SP', 'Coritiba PR', 'Cuiaba MT', 'Ceará CE',
'Atlética GO', 'Avaí SC', 'Juventude RS'
)
print(f'Os 5 primeiros colocados são {posicao[0:5]}\n')
print(f'Os 4 últimos são {posicao[-4:]}\n')
print(f'A tabela na ordem alfabética é {sorted(posicao)}')
print('-=' *68)
flamengo_posicao = posicao.index('Flamengo RJ') + 1
print(f"O time do Flamengo está na posição {flamengo_posicao}")

