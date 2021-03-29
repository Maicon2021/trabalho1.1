"""10.	Faça um programa que receba dois números inteiros e gere
os números inteiros que estão no intervalo
compreendido por eles.
"""
from time import sleep
n1 = int(input('Informe um Numero Inteiro: '))
n2 = int(input('Informe um Numero Inteiro Maior que o Anterior: '))
print(f'Os numeros no intervalo de {n1} e {n2} são')
n1 += 1
for numero in range(n1, n2):
    print(numero, end= ' ')
    sleep(0.5)