import os
#OS é uma variável que interage com o sistema OPeracionalll


mensagens = []

nome = input("Digite um nome para acessar o chat:")
#NOME fica fora do llop porque só se ped euma vez !!!
while True:
    #limpeza do terminal
    os.system('cls')
    
    #len quantifica os dados presentes numa lista
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print("______________")
    
    #obtendo texto
    
    texto = input("mensagem: (digite 'fim' para encerrar o chat !!!")
    
    if texto == "fim":
        break
    
    
    #adicionando mensagem na lista
    
    mensagens.append({
        "nome" : nome,
        "texto" : texto
    })
