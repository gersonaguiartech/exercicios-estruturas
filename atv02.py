#Questao2
#[1,2,3,4,16,32,64,128,256,500]
#[1,2,3,4,...]
#[1,4,9,16,...]
tam = 10
vetor_1 = [int] * tam
vetor_2 = [int] * tam
for i in range(len(vetor_1)):
    vetor_1[i] = int(input("Digite o valor \t"))
    #print(vetor_1)
print(vetor_1)
for j in range(len(vetor_2)):
    vetor_2[j] = [j] * vetor_1[j]