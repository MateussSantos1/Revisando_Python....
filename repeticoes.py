# ---------------REPETIÇÕES POR FOR--------------

#for x in range(5):
#    print(x)
    
notas = []
#nota vazia para ser preenchida no final 
for x in range(3):
    #while contador <=5:
    #ai botava o contador = contador +1
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultados  = [codigo_aluno, nota]
    #armazena os valores recebidos do usuario
    notas.append(resultados)
    #adiciona no fim da lista os dados recebidos a cada repetição
print("Quantidade de Notas:", len(notas))


print("DADOS DOS ALUNOS:")
contador = 0

while contador < len(notas):
    print(f"Aluno com RM {notas[contador][0]} tirou nota {notas[contador][1]}")
    #---------------------contador pega a partir da posição do aluno, isso varia de 0  a infinito, ja a segunda chave
    #pega aonde está posicionada a informação que se quer pegar do aluno de numero tal
    contador += 1
