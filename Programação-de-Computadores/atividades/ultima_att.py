"""
Faça um método que receba como parâmetros o Km inicial,
 Km final, quantidade de litros gastos e preço do litro. 
 Calcule e mostre: 

- Distância percorrida;

- Consumo médio;

- Valor gasto;

Faça um programa principal que solicite para o usuário o valor 
da quilometragem inicial, final, a quantidade de litros gastos e o 
preço do litro e mostre a distância percorrida, o consumo médio e o valor
 gasto, para isso utilize o método definido acima.
"""



def calcular_viagem (km_inicial, km_final, litros, preco):
    km_percorrido = km_final - km_inicial
    consumo = km_percorrido / litros if litros > 0 else 0
    gasto = consumo * preco

    print (f"\nA distância percorrida foi de {km_percorrido:.2f}km, o seu consumo foi de {consumo:.2f}(km/l) e o valor gasto nessa viagem foi de R${gasto:.2f}.")

km_inicial = float(input("Digite o km inicial da viagem: "))
km_final = float(input("Digite o km final da vigem: "))
litros = float(input("Digite quantos litros foi gasto nesta viagem: "))
preco = float(input("Digite o preço do litro: R$"))

calcular_viagem(km_inicial, km_final, litros, preco)


"""
Escreva um método com retorno que receba como parâmetros 
os lados de um retângulo, calcula e retorna o valor de sua área. 

 area = lado*lado

Faça um programa principal que solicite os valores dos lados de um 
retângulo ao usuário, e utilizando a função definida acima, calcule e 
mostre o valor de área.
"""

def calcular_area(ladoA, ladoB):
    area = ladoA * ladoB

    print(f"O valor da área deste retângulo é de {area:.2f}.")

ladoA = float(input("Digite o valor do 1º lado do retângulo: "))
ladoB = float(input("Digite o valor do 2º lado do retângulo: "))

calcular_area(ladoA, ladoB)


"""
Construir um método que receba como parâmetros o valor
 de uma compra e a quantidade de parcelas e calcula e retorna 
 o valor da parcela, sabendo que a loja acrescenta 5% de juros
   para as compras parceladas.

No algoritmo principal, solicite para o usuário o valor de uma 
compra e a quantidade de parcelas e utilizando o método descrito 
acima, mostre o valor da parcela.
"""

def calcular_compra(valor, qtd_parcelas):
    parcela = (valor / qtd_parcelas) * 1.05

    print(f"O valor das compras parcelado em {qtd_parcelas}º é de R${parcela:.2f}.")

valor = float(input("Digite o valor da compra: R$"))
qtd_parcelas = int(input("Digite em quantas vezes o cliente deseja parcelar a compra: "))

calcular_compra(valor, qtd_parcelas)


"""
Elabore um programa para calcular a velocidade de três 
objetos diferentes (com velocidade constante).



Conhecemos (são dados digitados pelo usuário), para cada objeto, 
a distância percorrida e o tempo que necessitou para percorrer 
essa distância.



Utilize um método geral que calcule e retorne a velocidade de um 
objeto, fornecidos como parâmetros os dados de distância e tempo.
"""


def calcular_velocidade(distancia, tempo):
    if tempo <= 0:
        return 0 
    return distancia / tempo

velocidade_obj = []

for i in range(1,4):
    print(f"\nDados do Objeto {i}:")
    distancia = float(input(f"Digite a distância percorrida pelo objeto {i} (em metros): "))
    tempo = float(input(f"Digite o tempo gasto pelo objeto {i} (em segundos): "))

    velocidade = calcular_velocidade(distancia, tempo)
    velocidade_obj.append(velocidade)

for i, vel in enumerate(velocidade_obj, 1):
    print(f"Objeto {i}: Velocidade = {vel:.2f} m/s")
