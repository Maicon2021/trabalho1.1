"""
1.	Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
"""
nota = 0
while nota >= 0 and nota <= 10:
    nota = int(input("Informe uma nota entre 0 e 10: "))
else:
    print('Nota fora da faixa de 0 a 10')