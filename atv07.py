distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

cidade1 = int(input("Digite a cidade de origem (0 a 4): "))
cidade2 = int(input("Digite a cidade de destino (0 a 4): "))

print("Distância =", distancias[cidade1][cidade2], "km")