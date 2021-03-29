cont = 0
n = 100
ultimo = 0
penultimo = 1
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo)