print('Exercicio 5')
opcao = 's'
while opcao in 'sS':
    print('------------ Sistema de Abastecimento ------------')
    tipoCombustivel = input('Tipo de Combustível: A - Álcool   G - Gasolina  S - Sair(Exit)')

    if tipoCombustivel in 'aAGg':
        litros = float(input('Informe Quantos Litros: '))

        #Opção Álcool
        if tipoCombustivel in 'aA':
            print('-----------------------------')
            #Valor do litro de Alcool, sem desconto R$ 1.90 e 3% de desconto
            if litros <= 20:
                valor = litros * 1.90
                valorDesconto = valor - (valor * 3) / 100
                print(f'Litros de Alcool: {litros} \nVlrUni R$: 1.90 \nValor Total R$: {valor} \nValor Total com Desconto R$: {valorDesconto}')

            #Valor do litro de Alcool, sem desconto R$ 1.90 e 5% de desconto
            else:
                valor = litros * 1.90
                valorDesconto = valor - (valor * 5) / 100
                print(f'Litros de Alcool: {litros} \nVlrUni R$: 1.90 \nValor Total R$: {valor} \nValor Total com Desconto R$: {valorDesconto}')

        #Opcão Gasolina
        else:
            print('-----------------------------')
            #Valor do litro da Gasolina, sem desconto R$ 2.50 e 4% de desconto
            if litros <= 20:
                valor = litros * 2.50
                valorDesconto = valor - (valor * 4) / 100
                print(f'Litros de Gasolina: {litros} \nVlrUni R$: 2.50 \nValor Total R$: {valor} \nValor Total com Desconto R$: {valorDesconto}')

            # Valor do litro da Gasolina, sem desconto R$ 2.50 e 6% de desconto
            else:
                valor = litros * 2.50
                valorDesconto = valor - (valor * 6) / 100
                print(f'Litros de Gasolina: {litros} \nVlrUni R$: 2.50 \nValor Total R$: {valor} \nValor Total com Desconto R$: {valorDesconto}')

    #Finalizando Programa
    elif tipoCombustivel in 'sS':
        print('Finalizando...')
        break

    #Sinalizando Opção Inválida
    else:
        print('Opção Inválida...')