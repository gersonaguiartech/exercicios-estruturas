def traduzir(lSecreta):

    tabela_letras = " abcdefghijklmnopqrstuvwxyz" 
    
    mensagem_revelada = ""
    
    for numero in lSecreta:
        mensagem_revelada += tabela_letras[numero]
        
    return mensagem_revelada

lista_teste = [2, 15, 13, 0, 4, 9, 1] # [cite: 45]
resultado = traduzir(lista_teste)
print(f"A mensagem secreta decodificada é: '{resultado}'")