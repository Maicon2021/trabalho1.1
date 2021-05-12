'''
Nome: Maicon R. Andreis
Data: 12/05/2021
'''
from time import sleep
#Criando Lista de Pessoas
lista_pessoa = []
#Criando Dicionario de pessoa
pessoa = {
    'nome': ' ',
    'data nascimento': ' ',
    'situacao': ''
}

for cout in range(1, 4): #repetindo a entrada de dados
    pessoa['nome'] = input('Informe Nome: ')

    while True:#Repetição de Validação da data
        nascimento = input('Informe data de nascimento DD/MM/AAAA: ')
        d, m, a = map(int, nascimento.split('/')) #separa apenas os valores numéricos e transforma em inteiro
        dia, mes, ano = int(d), int(m), int(a) #muda para inteiro os dia, mês e ano

        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano < 2021: #se validação idade Ok, sai da repetição
            break
        else: #Mensagem de erro da idade
            print('Data Inválida...\nDia, Mês ou Ano Inválidos....')

    pessoa['data nascimento'] = nascimento #Isere data ao dicionario pessoa['data nascimento']
    maior_idade = 2021 - ano #Calcula Idade

    #Incrementa Classificação idosa se idosa
    if 60 <= maior_idade <= 74:
        pessoa['situacao'] = 'Idosa'

    #add um dicionario Pessoa a Lista Pessoa
    lista_pessoa.append(pessoa.copy())

#Formatação apresentação da Lista
print(f"{60 * '-'}\n                 *** Apresentando Lista ***\n{60 * '-'}")
print('Nome                         | Data Nascimento')
print(60 * '=')

#percore lista para apresentação
for pessoa in lista_pessoa:
    print(f"{pessoa.get('nome')} {((29 - len(pessoa.get(('nome'))))*' ')} {pessoa.get('data nascimento')}   {pessoa.get('situacao')}")
    print(60*'-')

print('Finalizando...')
sleep(15)