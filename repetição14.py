n = 1
impar = 0
par = 0
while n <= 10:
    numero = int(input('Informe um Numero: '))
    n += 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'{par} Numeros Pares e {impar} Impares')