#são blocos de códigos que podem ser reutilizados pra realizarem tarefas especificas!


#criando a funcao:
def funcao_soma (n1, n2):
    return n1 + n2
loop = True
while loop == True:
    val1 = int(input("Digite um valor: "))
    val2 = int(input("Agora, por fim, digite outro valor: "))
    resultado = funcao_soma(val1, val2)
    print (f"A soma desses 2 valores é {resultado:.2f}")
    confirm = input("Continuar?? ('S' ou 'N')").upper()
    #UPPER padroniza em maiúsculo !!!
    if confirm == 'N':
        loop = False