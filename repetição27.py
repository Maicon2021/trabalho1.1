"""27.	Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos."""

qtde_turma = int(input('Informe a Quantidade de Turmas: '))
alunos_turma = []
turma = 1
for i in range(1, qtde_turma + 1):
    print('Turma ', turma)
    alunos = int(input('Quantos alunos Possui: '))
    while alunos > 40:
        print('Turma ', turma, 'A turma não pode ter mais que 40 Alunos... ')
        alunos = int(input('Alunos da Turma: '))
    turma += 1
    alunos_turma.append(alunos)

media = sum(alunos_turma) / len(alunos_turma)
print(f'A media de Alunos por turma é: {media}')
