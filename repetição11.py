from time import sleep
n1 = int(input('Informe um Numero Inteiro: '))
n2 = int(input('Informe um Numero Inteiro Maior que o Anterior: '))
print(f'Os numeros no intervalo de {n1} e {n2} são')
n1 += 1
soma = 0
for numero in range(n1, n2):
    print(numero, end= ' ')
    soma += numero
    sleep(0.5)

print(f'Soma dos Numeros no intervalo é: {soma}')