"""

1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
• não-eleitor (abaixo de 16 anos)
• eleitor obrigatório (entre 18 e 65 anos)
• eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo
grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou
zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta
negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a
zero.
3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
Valor de vendaValor de compra
lucro de 70%valor < R$10,00
lucro de 50%R$ 10,00 <= valor < R$ 30,00
lucro de 40%R$ 30,00 <= valor < R$ 50,00
lucro de 30%valor >= R$50,00
Crie uma programa que permita digitar o nome do produto e valor da compra, e
imprimindo o nome do produto e o valor da venda.
4- Elabore um programa em Python que implemente uma calculadora com as funções de
somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e
mostrar o resultado.
"""

"""
 1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
• não-eleitor (abaixo de 16 anos)
• eleitor obrigatório (entre 18 e 65 anos)
• eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
"""

idade = int (input("Digite a sua Idade: "))
if idade < 16:
    print ("Não eleitor")
elif 18 <= idade <= 65:
    print ("Eleitor obrigatório")
else:
    print ("Eleitor facultativo")
"""
2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo
grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou
zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta
negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a
zero.
"""

import math

a = int (input("Digite o valor de A: "))
b = int (input("Digite o valor de B: "))
c = int (input("Digite o valor de C: "))
if a == 0:
   print("Não é equação do segundo grau")
else:
    delta = math.pow(b,2) - 4 * a * c
    if delta < 0:
        print ("Não há raízes reais")
    else:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b + raiz) / (2 * a)
        print ("As raízes desta conta é x1:%.2f e de x2:%.2f" % (x1, x2))

"""
3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
Valor de vendaValor de compra
lucro de 70%valor < R$10,00
lucro de 50%R$ 10,00 <= valor < R$ 30,00
lucro de 40%R$ 30,00 <= valor < R$ 50,00
lucro de 30%valor >= R$50,00
Crie uma programa que permita digitar o nome do produto e valor da compra, e
imprimindo o nome do produto e o valor da venda.
"""

produto = input("Digite o nome do Produto: ")
valor = float (input("Digite o valor do Produto: "))
if valor < 10:
    lucro = valor * 0.70
    print("O seu lucro cima do Produto %s é de R$%.2f" % (produto,lucro))
elif 10 <= valor < 30:
    lucro = valor * 0.50
    print("O seu lucro cima do Produto %s é de R$%.2f" % (produto,lucro))
elif 30 <= valor < 50:
    lucro = valor * 0.40
    print("O seu lucro cima do Produto %s é de R$%.2f" % (produto,lucro))
else:
    lucro = valor * 0.30
    print("O seu lucro cima do Produto %s é de R$%.2f" % (produto,lucro))

""""
4- Elabore um programa em Python que implemente uma calculadora com as funções de
somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e
mostrar o resultado.
"""

num1 = float(input("Digite o valor do primeiro número:"))
num2= float(input("Digite o valor do segundo número: "))
funcao = input("Digite qual função será usada ('+', '-', '*', '/'):")
if funcao == '+':
    calculo = num1 + num2
    print (calculo)
elif funcao == '-':
    calculo = num1 - num2
    print (calculo)
elif funcao == '*':
    calculo = num1 * num2
    print (calculo)
elif funcao == '/':
    calculo = num1 / num2
    print (calculo)
else : 
    print ("Digite ")
