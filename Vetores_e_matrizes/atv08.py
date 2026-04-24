def corrigir_provas():
    gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'] 
    
    for i in range(3): 
        print(f"\n--- Corrigindo prova do Aluno {i+1} ---")
        matricula = int(input("Digite a matrícula do aluno: "))
        
        respostas_aluno = []
        acertos = 0
        
        for q in range(10):
            resposta = input(f"Resposta da questão {q+1} (a, b, c, d, e): ").lower()
            respostas_aluno.append(resposta)
            
            if resposta == gabarito[q]:
                acertos += 1
                
        percentual = (acertos / 10) * 100
        status = "APROVADO" if acertos >= 7 else "REPROVADO"
        
        print("\n-- BOLETIM --")
        print(f"Matrícula: {matricula}")
        print(f"Respostas do aluno: {respostas_aluno}")
        print(f"Nota final: {acertos:.1f} (Percentual: {percentual}%)")
        print(f"Situação: {status}")