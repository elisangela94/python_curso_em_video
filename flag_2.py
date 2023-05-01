# ler varios números
# Só para quando digitar o número 999 
# Usar comando brak
n1 = num = 0
while True: 
    num = int(input('digite um número: '))
    if num == 999:
        break
    n1 += num
print(f'A soma entre eles é {n1}')