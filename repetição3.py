"""
3.	Faça um programa que leia e valide as seguintes informações:
o	Nome: maior que 3 caracteres;
o	Idade: entre 0 e 150;
o	Salário: maior que zero;
o	Sexo: 'f' ou 'm';
o	Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    letra = str(input('Informe nome: '))

    if len(letra) > 3:
       break
    else:
        print('Nome precisa conter mais que 3 carecteres.')

while True:
    idade = int(input('Informe idade em anos: '))

    if idade > 0 and idade < 150:
        break
    else:
        print('Indade precisa estar entre 0 e 150.')