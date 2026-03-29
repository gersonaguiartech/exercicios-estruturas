def traduzir(lSecreta):
    # O índice 0 é um espaço, o 1 é 'a', 2 é 'b', etc.
    # Uma string funciona perfeitamente!
    tabela_letras = " abcdefghijklmnopqrstuvwxyz" 
    
    mensagem_revelada = ""
    
    for numero in lSecreta:
        # Pega a letra correspondente ao número e junta na mensagem
        mensagem_revelada += tabela_letras[numero]
        
    return mensagem_revelada

# Testando o código das amigas
lista_teste = [2, 15, 13, 0, 4, 9, 1] # [cite: 45]
resultado = traduzir(lista_teste)
print(f"A mensagem secreta decodificada é: '{resultado}'")