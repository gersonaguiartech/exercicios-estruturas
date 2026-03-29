import random

numeros = random.sample(range(100), 25)

cartela = []
k = 0

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(numeros[k])
        k += 1
    cartela.append(linha)

print("Cartela de bingo:")
for linha in cartela:
    for num in linha:
        print(f"{num:02}", end=" ")
    print()