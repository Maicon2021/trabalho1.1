while True:
    p_a = int(input('Infome a Quantidade de Habitantes do Pais A: '))
    t_crescimento = float(input('Informe a taxa de Crescimento do Pai A: '))
    p_b = int(input('Infome a Quantidade de Habitantes do Pais B: '))
    t_crescimento_b = float(input('Informe a taxa de Crescimento do Pai B: '))

    opcao = 1
    anos = 0
    while p_b >= p_a:
        p_a = p_a + (p_a * (t_crescimento / 100))
        p_b = p_b + (p_b * (t_crescimento_b / 100))
        anos = anos + 1

    print(f'Em {anos} Anos O Pais A tera {p_a:.0f} Habitantes e vai Ultrapassar ao Pais B com {p_b:.0f} Habitantes')
    opcao = int(input('Escolha a Opçao: 0 - Sair 1 - Continuar: '))
    if opcao == 0:
        break