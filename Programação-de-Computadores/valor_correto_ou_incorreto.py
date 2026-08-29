#Escreva um algoritmo que solicite um número ao usuário. 
# Caso seja digitado um valor entre 0 e 9, 
# mostre: “valor correto”, caso contrário mostre: “valor incorreto”.

num = int(input("Digite um número: "))
if 0 <= num <= 9:
    print ("Valor correto")
else:
    print ("Valor Incorreto")