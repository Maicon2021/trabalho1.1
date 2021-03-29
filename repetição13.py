"""13.	Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem
"""
base = int(input('Informe o numero Base: '))
ex = int(input('Informe o Expoente do Numero anterior: '))
cont = 1
valor = 1

while cont <= ex:
    valor *= base
    cont += 1

print(f'{base} elevado a {ex} é = {valor}')