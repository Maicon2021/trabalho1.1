"""26.	Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato"""
n_eleitores = int(input('Informe o Numero de Eleitores: '))
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
nulo = 0

for i in range(0, n_eleitores):
    voto = int(input('Para Votar:\n ( 1 ) Candidato_1  ( 2 ) Candidato_2  ( 3 ) Candidato_3: '))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    else:
        nulo += 1

print(f'Numero de Votos:\nCandidato_1 = {candidato_1} \nCandidato_2 = {candidato_2} \nCandidato_3 = {candidato_3} \nNulos = {nulo}')