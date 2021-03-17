print('Exercicio 3')
n1 = float(input('Informe primeiro Número: '))
n2 = float(input('Informe segundo Número: '))

opcao = str(input('Informe qual Operação \n( + )Soma \n( - ) Subtração \n( * ) Multiplicação \n( / ) Divisão '))

resultado = 0

if opcao == '+':
    resultado = n1 + n2
    print(f'O valor da Soma = {resultado}')

elif opcao == '-':
    resultado = n1 - n2
    print(f'O valor da Subtração = {resultado}')

elif opcao == '*':
    resultado  = n1 * n2
    print(f'O valor da Multiplicação = {resultado}')

elif opcao == '/':
    resultado = n1 / n2
    print(f'O valor da Divisão = {resultado}')
else:
    print('Oção Invalida...')

if resultado % 2 == 0:
    print('É Par...')
else:
    print('É Impar...')

if resultado // 1 == resultado:
    print('Inteiro...')
else:
    print('Decimal...')

if resultado < 0:
    print('Negativo...')
else:
    print('Positivo...')
