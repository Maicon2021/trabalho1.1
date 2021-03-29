soma = 0
for i in range(1, 7):
    n = int(input('Informe um numero: '))
    if n % 2 == 0:
        soma += n
print(f'O A soma dos Valores Pares digitados, são: {soma}')