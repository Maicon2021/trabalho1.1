"""25.	Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""
media_turma = 0
soma = 0
n_alunos = 0
while True:
    idade = int(input('0 - Finaliza. Informe a Idade: '))
    if idade == 0:
        break
    else:
        soma += idade
        n_alunos += 1
media_turma = soma / n_alunos
if media_turma <= 25:
    print(f'A media de Idade da Turma é {media_turma} - Jovem...')
elif media_turma > 25 and media_turma <= 60:
    print(f'A media de Idade da Turma é {media_turma} - Adulta...')
else:
    print(f'A media de Idade da Turma é {media_turma} - Idosa...')