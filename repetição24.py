cont = 0
media = 0
soma = 0
while True:
    nota = float(input('11 - Finaliza, Informe as Nota para saber a Média: '))
    if nota == 11:
        break
    soma += nota
    cont += 1
media = soma / cont
print(f'{cont} Notas Digitas, a Media é: {media:.1f}')