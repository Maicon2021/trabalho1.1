n = int(input("Digite Numero de vezes a repetir: "))
maior = None
menor = None
for i in range(n):
   x = int(input("Digite um número: "))
   maior = maior if maior != None and maior >  x else x
   menor = menor if menor != None and menor < x else x

print ('O maior valor foi {} e o menor {}'.format(maior, menor))
