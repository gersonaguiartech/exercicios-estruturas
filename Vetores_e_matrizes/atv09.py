def proxima_jogada(tabuleiro):
    # Uma inteligência artificial simples, mas simpática!
    # Ela varre a matriz procurando a primeira casa vazia (0) para jogar.
    
    print("Analisando o tabuleiro...")
    
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0: # [cite: 76]
                print(f"Minha sugestão: Coloque sua peça na Linha {linha}, Coluna {coluna}.")
                return 
                
    print("Opa, o tabuleiro já está cheio! Deu velha.")

tabuleiro_atual = [
    [ 1, -1,  1],
    [-1, -1,  0],
    [ 0,  1,  0]
]

proxima_jogada(tabuleiro_atual)