n_cds = int(input('Informe a Quantidade de CDs?: '))

v_medio = 0
v_total = 0

for i in range(1, n_cds + 1):
    v_cd = float(input(f'Quanto Custou o {i}° CD? R$: '))

    v_total += v_cd
    v_medio += v_cd / n_cds

print(f'Em {n_cds} CDs Foi Gasto R$: {v_total}')
print(f'O Valor Médio dos CDs foi de R$: {v_medio}')