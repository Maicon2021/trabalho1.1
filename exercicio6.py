from time import sleep
print('Exercicio 6')
print('Inciando Sitema....')
sleep(2)
sistema = 'c'
while sistema in 'cC':
    print('------------ Sistema de Frutaria ------------')
    sistema = input(' C - Continuar  S - Sair(Exit)')

    #Operação Continuar
    if sistema in 'cC':
        morango = float(input('Informe Quantos Kg de Morango: '))
        maca = float(input('Informe Quantos Kg de Maçã: '))

        #operação quantidade de Kg
        kgFrutas = morango + maca

        #Operação Morango
        if morango <= 5:
            print('---------------------------------')
            valorMorango = morango * 2.5
            print(f'Quantidade Morango em Kg: {morango}\nValor Kg R$: 2.50 \nValor Total R$: {valorMorango:.2f}')
        else:
            print('---------------------------------')
            valorMorango = morango * 2.20
            print(f'Quantidade Morango em Kg: {morango}\nValor Kg R$: 2.20 \nValor Total R$: {valorMorango:.2f}')

        #Operação Maçã
        if maca <= 5:
            print('---------------------------------')
            valorMaca = maca * 1.80
            print(f'Quantidade Maçã em Kg: {maca}\nValor Kg R$: 1.80 \nValor Total R$: {valorMaca:.2f}')
        else:
            print('---------------------------------')
            valorMaca = maca * 1.50
            print(f'Quantidade Maçã em Kg: {maca}\nValor Kg R$: 1.5 \nValor Total R$: {valorMaca:.2f}')

        #Opreração de Desconto caso maior que 8 kg e mais de 25 reais
        vlrTotal = valorMaca + valorMorango
        print('------ Valor Total ------')
        print(f'Valor Total de Compras R$: {vlrTotal:.2f}')
        if kgFrutas > 8 or vlrTotal > 25:
            vlrDesconto = vlrTotal - (vlrTotal * 10) / 100
            print(f'Valor com Desconto: {vlrDesconto:.2f}')

    #Finalizando Programa
    elif sistema in 'sS':
        print('Finalizando...')
        break

    #Sinalizando Opção Inválida
    else:
        sistema = 'c' #seta c para retornar ao inicio caso opção invalida
        print('Opção Inválida...')