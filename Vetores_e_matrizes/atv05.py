def verificar_quadrado_magico(matriz):
    soma_alvo = sum(matriz[0])
    
    for linha in matriz:
        if sum(linha) != soma_alvo:
            return False
            
    for coluna in range(3):
        soma_coluna = matriz[0][coluna] + matriz[1][coluna] + matriz[2][coluna]
        if soma_coluna != soma_alvo:
            return False
            
    diagonal_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
    
    if diagonal_principal != soma_alvo or diagonal_secundaria != soma_alvo:
        return False
        
    return True

matriz_exercicio = [
    [8, 0, 7], # [cite: 48]
    [4, 5, 6], # [cite: 48]
    [3, 10, 2] # [cite: 48]
]

if verificar_quadrado_magico(matriz_exercicio):
    print("Que legal! Esta matriz É um quadrado mágico.")
else:
    print("Poxa, esta matriz NÃO é um quadrado mágico.")