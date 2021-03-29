while True:
    numero = int(input("0 - Sai do loop, Informe o numero para saber seu Fatorial: "))
    resultado = 1
    if numero > 0 and numero < 16:
        for n in range(1, numero + 1):
            resultado *= n
        print(resultado)
    elif numero == 0:
        break
    else:
        print('Numero Invalido, Numero Positivo > 0 e < 16')