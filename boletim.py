# exercicio 89
# crie uma tabela com o boletim dos alunos cadastrados

table = [['NO.'],['NOME'],['MÉDIA']]
while True:
    for l in range(0,3):
        for c in range(0,3):
            table[0][1] = str(input('nome:'))
            nota_um = float(input('Nota 1: '))
            nota_dois = float(input('Nota 2: '))
            table[0][2] = (nota_um + nota_dois)/2
            resp = str(input('Deseja continuar? [S/N]: ')).upper()
            if resp == "N":
                break
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end= '') # :^5 = centraliza 
    print()