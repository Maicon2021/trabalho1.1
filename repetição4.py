"""4.	Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""
p_a = 80000
p_b = 200000
anos = 0
while p_b >= p_a:
    p_a += p_a * 0.03
    p_b += p_b * 0.015
    anos = anos + 1
print(f'Em {anos} Anos O Pais A {p_a:.0f} vai Ultrapassar ao Pais B {p_b:.0f}')