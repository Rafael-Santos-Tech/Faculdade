#Escreva um programa em Python que 
# solicite ao usuário os valores de 
# três contas de consumo 
# (p.ex. água, luz e telefone) e o 
# valor de seu salário. Verifique 
# se o salário é suficiente para 
# pagar as três contas, caso não 
# seja apresente a mensagem 
# “Salário insuficiente!”. 
# Caso seja, apresente o valor que 
# restou do salário após pagar as 
# contas.

print ("Digite três contas de consumo e o seu sálario")
conta_1 = float(input("Digite o valor da primeira conta de consumo: "))
conta_2 = float(input("Digite o valor da segunda: "))
conta_3 = float(input("Digite o valor da terceira: "))
salario = float(input("Digite seu sálario: "))
contas = conta_1 + conta_2 + conta_3
if salario < contas:
    print ("Sálario insuficiente!")
else:
    resto = salario - contas
    print ("Do seu sálario após pagar as 3 contas de consumo te resta R$%.2f" % resto)