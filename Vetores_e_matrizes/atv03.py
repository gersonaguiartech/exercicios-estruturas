def somar_posicoes_vetor():
    print("--- Calculadora de Posições do Vetor ---")
    vetor_numeros = []
    
    #o vetor com 8 números
    for i in range(8):
        numero = float(input(f"digite o {i+1}º número: "))
        vetor_numeros.append(numero)
        
    print("\notimo! Agora escolha duas posições (de 0 a 7) para somar os valores.")
    posicao_x = int(input("Qual é a primeira posição (X)? "))
    posicao_y = int(input("Qual é a segunda posição (Y)? "))
    
    # Validando
    if 0 <= posicao_x < 8 and 0 <= posicao_y < 8:
        soma = vetor_numeros[posicao_x] + vetor_numeros[posicao_y]
        print(f"\nO valor na posição {posicao_x} é {vetor_numeros[posicao_x]}.")
        print(f"O valor na posição {posicao_y} é {vetor_numeros[posicao_y]}.")
        print(f"A soma mágica desses dois é: {soma}")
    else:
        print("erro! As posições precisam estar entre 0 e 7. Tente novamente.")