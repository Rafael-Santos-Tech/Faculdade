# Exercicio 1
altura = float(input("Digite o valor da altura da pirâmide: "))
menor = float(input("Digite o valor da base menor da pirâmide: "))
maior = float(input("Digite o valor da base maior da pirâmide: "))
volume = (altura / 3) * (maior ** 2 + menor ** 2 + (maior ** 2 * menor ** 2) ** 0.5)
print ("O volume do tronco da pirâmide equivale a %.2f" % volume)