#Crie um algoritmo que 
# solicite ao usuário o seu turno de 
# trabalho e a quantidade de horas 
# trabalhadas, calcule e mostre o 
# valor do salário. Considere os 
# valores de horas a seguir, de acordo
#  com o turno de trabalho. Caso o 
# turno seja igual a ‘N’ 
# (utilize um caractere para 
# representar) o valor da hora 
# trabalhada é R$ 45,00, caso 
# contrário é R$ 37,50.

turno = input("Digite seu turno de trabalho se noturno digite N, se algum outro turno digite O: ")
hora_t = int(input("Digite sua quantidade de horas trabalhadas: "))
if turno == 'N' or turno == 'n':
    v_hora = 45.00
else:
    v_hora = 37.50
salario = v_hora * hora_t
print ("Você sendo deste turno o valor do seu salário é de R$%.2f " % salario)