def proxima_jogada(tabuleiro):
    # Uma inteligência artificial simples, mas simpática!
    # Ela varre a matriz procurando a primeira casa vazia (0) para jogar.
    
    print("Analisando o tabuleiro...")
    
    for linha in range(3):
        for coluna in range(3):
            # Encontrou uma casa vazia?
            if tabuleiro[linha][coluna] == 0: # [cite: 76]
                print(f"Minha sugestão: Coloque sua peça na Linha {linha}, Coluna {coluna}.")
                return # Encerra a função após sugerir o primeiro espaço livre
                
    print("Opa, o tabuleiro já está cheio! Deu velha.")

# Testando com um tabuleiro de exemplo
tabuleiro_atual = [
    [ 1, -1,  1], # 1 é oponente, -1 sou eu [cite: 76]
    [-1, -1,  0], # [cite: 78]
    [ 0,  1,  0]  # [cite: 78]
]

proxima_jogada(tabuleiro_atual)