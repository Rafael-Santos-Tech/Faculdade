#Faça um programa em Python que 
# obtenha o valor de uma compra, 
# calcular e mostrar o valor da 
# compra considerando o desconto, 
# conforme descrito abaixo: 
#Para compras acima de R$ 200 a 
# loja dá um desconto de 20%
#Para as abaixo disso não tem 
# desconto, mostre o valor da compra. 

compra = float(input("Digite o valor da compra:"))
if compra > 200: 
    valor_c = compra * 1.20
    print ("Valor da compra é R$%.2f" % valor_c)
else:
    print ("Valor da compra é R$", compra)