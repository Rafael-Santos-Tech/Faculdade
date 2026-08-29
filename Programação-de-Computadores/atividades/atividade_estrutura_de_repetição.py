"""
1.Faça um programa em Python que imprima os números pares entre 0 e 100
"""

for i in range (0,101,2):
    print (i, end=" ")

"""
2.Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a 100 de 2 em 2.
"""

for i in range (0,51):
    print (i, end=", ")
for i in range (52,101,2):
    print (i, end=", ")

"""
3.Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:

 S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n
 """

n = int(input("Digite o valor: "))
if n <= 0:
    print ("Digite um valor inteiro e positivo")
else: 
    soma = 0
    for i in range (1, n + 1):
        soma += 1 / i
        print ("Resultado da soma S=", soma)

"""
4.Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são 
positivos e quantos são negativos. Determine, também, qual é o menor desses valores. 
Utilize o comando de repetição que desejar.
"""

valores = int (input("Digite a quantidade de valores desejado: "))
positivos = 0
negativos = 0
menor = None
for i in range (valores):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    if menor is None or valor < menor:
        menor = valor
print (f"Quantidade de valores positivos:{positivos}\nQuantidade de valores negativos:{negativos}\nMenor valor:{menor}")

"""
5.Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa, 
calcule e mostre a altura média das mulheres e dos homens separadamente. 
Utilize o comando de repetição que desejar
"""

quantidade = int(input("Digite a quantidade de pessoas que será informada no grupo: "))
soma_h = 0
soma_m = 0
quantidade_h = 0 
quantidade_m = 0 
for i in range (quantidade):
    sexo = input(f"Digite o sexo da {1+i}º pessoa usando (M/F): ").upper()
    altura = float (input(f"Digite a altura da {1+i}º pessoa: "))
    if sexo == 'M':
        soma_h += altura
        quantidade_h += 1
    elif sexo == 'F':
        soma_m += altura
        quantidade_m += 1
    else: 
        print ("Sexo inválido.")
if quantidade_h > 0 :
    media_h = soma_h / quantidade_h
    print ("Altura média dos Homens é de:", media_h)
else: 
    print ("Nenhum Homem foi informado")
if quantidade_m > 0 :
    media_m = soma_m / quantidade_m
    print ("Altura média das Mulheres é de:", media_m)
else:
    print ("Nenhuma Mulher foi informada")
