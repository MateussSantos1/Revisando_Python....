
#variáveis:

nome = str(input("Qual o seu nome???"))
idade = int(input("Qual a sua idade???"))

if idade < 18:
    maior_idade = False
    print("Não aceito !!!! MENOR IDADE!!!!")
    exit()
if idade > 18:
    maior_idade = True
    peso = float(input("Qual o seu peso???"))
    print(f"O seu nome é {nome}, sua idade é {idade} anos e seu peso é {peso:.2f}KG")








