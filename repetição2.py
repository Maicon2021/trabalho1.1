nome = str(input('Informe seu Nome: '))
while True:
    senha = str(input('Infome senha: '))
    if senha != nome:
        print('Senha aceita...')
        break
    else:
        print('## Erro ## - Senha não pode ser igual nome... ')
print('Iniciando Sistema....')
