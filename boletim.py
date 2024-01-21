# exercicio 89
# crie uma tabela com o boletim dos alunos cadastrados

table = list()
while True:
    nome = str(input('nome:'))
    nota_um = float(input('Nota 1: '))
    nota_dois = float(input('Nota 2: '))
    media = (nota_um + nota_dois)/2
    table.append([nome, [nota_um, nota_dois], media])
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp == "N":
        break
print('-='*30)
print(f'{"NO":<4}{"NOME":<10}{"MÉDIA":>8}') # ':< ' = alinhado a esquerda
print('-'*26)
for i, a in enumerate(table):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}') # i = valor da váriavel e 'a' será os valores que contém dentro
while True:
    print('-'*30)
    aluno = str(input('Deseja mostrar a nota de algum aluno detalhada [S/N]? ')).upper()
    while aluno not in 'SN':
        aluno = str(input('Deseja mostrar a nota de algum aluno detalhada [S/N]? ')).upper()
    if aluno == 'N':
        print('FINALIZANDO...')
        break
    if aluno == 'S':
        escolha = int(input('De qual aluno deseja a nota?'))
        if escolha <= len(table)-1:
            print(f'A nota de {table[escolha][0]} são {table[escolha][1]}')
print('Volte sempre!')