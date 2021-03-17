print('Exercicio 4')
opcao = 's'
while opcao == 's' or opcao == 'S':

    p1 = str(input('Telefonou para Vítima \nS - Sim?\nN - Não?'))
    p2 = str(input('Esteve no Local do Crime \nS - Sim?\nN - Não?'))
    p3 = str(input('Mora perto da Vítima \nS - Sim?\nN - Não?'))
    p4 = str(input('Deve para Vítima \nS - Sim?\nN - Não?'))
    p5 = str(input('Já Trabalhou com a Vítima \nS - Sim?\nN - Não?'))
    variavel = 0

    if p1 == 's' or p1 == 'S':
        variavel = variavel +1

    if p2 == 's' or p2 == 'S':
        variavel = variavel + 1

    if p3 == 's' or p3 == 'S':
        variavel = variavel + 1

    if p4 == 's' or p4 == 'S':
        variavel = variavel + 1

    if p5 == 's' or p5 == 'S':
        variavel = variavel + 1

    if variavel == 2:
        print('Suspeito...')
    elif variavel == 3 or variavel == 4:
        print('Cúmplice...')
    elif variavel == 5:
        print('Assassino...')
    else:
        print('Inocente...')

    opcao = str(input('Deseja continuar \nS - Sim? N - Não?'))
    if opcao == 'n' or opcao == 'N':
        print('Fim do Programa...')
        break


