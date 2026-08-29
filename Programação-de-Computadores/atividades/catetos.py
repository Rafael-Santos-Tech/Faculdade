# Exercicio 5
import math
angulo_g = float(input("Digite o valor do angulo em graus: "))
angulo_r = math.radians(angulo_g)
seno = math.sin(angulo_g)
cosseno = math.cos(angulo_g)
tangente = math.tan(angulo_g)
print ("O valor do seu ângulo em \nRadianos:%.2f° \nSeno:%.2f° \nCosseno:%.2f° \nTangente:%.2f° " % (angulo_r,seno,cosseno,tangente))