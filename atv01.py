numeros = [1,2,4,16,32,64,-128]
tam = 7 #indica o tamanho do vetor
vetor_numero = [0] * tam
for i in range(tam):
    vetor_numero[i] = int(input("digite o valor \t"))
#[1,2,4,16,32,64,-128]
valor_a = vetor_numero[0]
valor_b = vetor_numero[0]
pos_maior = vetor_numero[0]
pos_menor = vetor_numero[0]
for i in range(0,len(vetor_numero)):
    if vetor_numero[i] > valor_a:
        valor_a = vetor_numero[i]
        pos_maior = i
    if vetor_numero[i] < valor_b:
        valor_b = vetor_numero[i]
        pos_menor = i
    print("o resultado de valor_a " , valor_a)
    print("a posiçao do maior valor", pos_maior)
    print("o resultado de valor_b " , str(valor_b))
    print("a posiçao do menor valor",pos_menor)