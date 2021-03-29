cont = 0
n = 10
ultimo = 0
penultimo = 1

for count in range(0,n):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo)