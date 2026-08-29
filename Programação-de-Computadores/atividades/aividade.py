"""
Faça um programa em Python que contenha 3 listas com os nomes:
 valores, par e impar. 
Solicite N números inteiros ao usuário e armazene-os na lista
 chamada valores 
(utilize como critério de parada se o usuário deseja continuar). 
Após a obtenção dos dados, na lista par armazene apenas 
os números pares da lista valores 
e na lista ímpar os números ímpares. É obrigatório o
 uso de estrutura de repetição e listas.
§Exiba os números armazenados nas 3 listas.
"""

valores = []
par = []
impar = []

while True:
    try: 
        num = int(input("Digite um número inteiro: "))
        valores.append(num)

        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    
    except ValueError:
        print (("Digite apenas números inteiros."))
        continue

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar == 'n':
         break

print ("~" * 30)
print (f"Lista completa com os valores: {valores}")
print (f"Valores pares: {par}")
print (f"Valores ímpares: {impar}")
print ("~" * 30)


"""
Faça um programa que:

Leia duas listas com 5 inteiros cada.

Checa quais elementos da segunda lista são iguais a algum elemento
 da primeira lista.

Se não houver elementos em comum, o programa deve informar isso.

    Entrada

 Saída

   [1, 2, 3, 4, 5]

[0, 7, 6, 10, 3]

 3

    Entrada

 Saída

   [1, 2, 3, 4, 5]

[0, 7, 6, 10, 8]

 Não há elemento em comum.


"""

lista_1 = []
lista_2 = []
comuns  = []

print ("Digite 5 números inteiros para a 1º lista")
for i in range (5):
    num1 = int(input("Digite o número: "))
    lista_1.append(num1)

print ("\nDigite 5 números inteiros para a 2º lista")
for i in range (5):
    num2 = int(input("Digite o número: "))
    lista_2.append(num2)

for elemento in lista_2:
    if elemento in lista_1:
        if elemento not in comuns:
            comuns.append(elemento)

print("\n Saída:")
if len(comuns) >  0:
    for item in comuns:
        print(item)
else:
    print ("Não há elemento em comum")


"""
Faça um programa em Python que solicite ao usuário a placa e o valor 
da multa de 15 carros. As informações obtidas devem ser armazenadas 
em 2 listas distintas (observe que cada lista poderá ter apenas 15 
itens armazenados e que na posição i das duas listas ficarão armazenados:
 a placa i e o valor de venda i, veja exemplo abaixo). 

É obrigatório o uso de estrutura de repetição e listas. Calcule
 e mostre e o valor médio de todas as multas e quantos carros possuem o
   valor de multa maior ou igual a R$300.00, para isso utilize os dados 
   armazenados nas listas descritas  e estrutura de repetição.



    0

 AAA-1234

   1

 CCC-1234

   2

 AAA-1234

   3

 DDD-1234

   ...

   

   14

 BBB-1234

    0

880.41

   1

1467.35

   2

293.47

   3

293.47

   ...

   

   14

2934.70

  
"""

placas = []
multas = []

print ("Digite a placa e o valor das multas de 15 carros.")
for i in range (15):
    placa = input(f"Digite a placa do {i+1}º carro: ")
    multa = float(input("Digite o valor da multa do carro: R$"))
    placas.append (placa)
    multas.append (multa)

soma_total = 0
contagem_alta = 0

for multa in multas: 
    soma_total += multa
    if multa >= 300.00:
        contagem_alta += 1

media = soma_total / 15    

for i, placa in enumerate(placas):
    print(f"\n{i+1}º carro: {placa}")
for i, multa in enumerate(multas):
    print(f"\nValor da multa do {i+1}º carro: R${multa}")
print(f"\nValor médio das multas: R$ {media:.2f}")
print(f"\nQuantidade de carros com multas >= R$ 300,00: {contagem_alta}")


"""
Faça um programa em Python que solicite ao usuário o dia da semana e o
volume de chuva correspondente a 10 dias. As informações obtidas devem ser
 armazenadas em 2 listas distintas (observe que cada lista poderá ter apenas
 10 itens armazenados e que na posição i das duas listas ficarão 
 armazenados: o dia da semana i e o volume de chuva i). É obrigatório o 
 uso de estrutura de repetição e listas.

Em seguida, calcule e mostre o volume médio de chuva apenas do dia de 
semana igual a quarta-feira e a soma total do volume de chuva, para isso 
utilize os dados armazenados nas listas. É obrigatório o uso de estrutura 
de repetição e das listas do exercício descritas anteriormente.
"""

dias =   []
volume = []

print ("Digite o dia da semana e o volume de chuva correspondente a 10 dias")
for i in range (10):
    dia = input(f"Digite qual é o {i+1}º dia: ").strip().lower()
    chuva = float(input(f"Digite o volume de chuva (mm) para {dia}: "))
    dias.append(dia)
    volume.append(chuva)

soma_total = 0
quarta = 0
volume_quarta = 0

for i in range(len(dias)):
    soma_total += volume[i]

    if dias [i] == 'quarta-feira' or dias [i] == 'quarta':
        quarta += 1
        volume_quarta += volume[i]

if quarta > 0:
    media_quarta = volume_quarta / quarta
else:
    media_quarta = 0

print (f"A média do volume de chuva de quarta-feira é {media_quarta:.2f} e o total do volume de chuva neste periodo é {soma_total:.2f} ")


"""
Criar um programa em Python que leia os dados necessários para 
cadastrar os nomes de N alunos em uma lista, em outra lista as 
respectivas notas dos alunos e em uma terceira lista o seu curso 
(ccp ou tads). Observe que na posição i das três listas ficarão 
guardados: o nome do aluno i, a nota do aluno i e o curso do aluno i.

Resolva os seguintes itens:

a)Calcule e visualize a quantidade de alunos do curso de tads.

b)Calcule e visualize a média das notas dos N alunos.

c)Quantos alunos estão com a nota acima da média.
"""

alunos = []
notas = []
cursos = []

qtd = int(input("Digite a quantidade de alunos que deseja catalogar: "))
for i in range(qtd):
    aluno = input (f"\nDigite o nome do {i+1}º aluno: ")
    nota = float (input(f"Digite na nota do {aluno}: "))
    curso = input (f"Digite o curso do aluno {aluno} se (ccp/tads): ").strip().lower()
    alunos.append(aluno)
    notas.append(nota)
    cursos.append(curso)

qtd_tads = 0
soma_notas = 0
acima_media = 0

for curso in cursos:
    if curso == 'tdas':
        qtd_tads += 1

for i in range(len(notas)):
    soma_notas += notas[i]
    media = soma_notas / qtd

    if nota > media:
        acima_media += 1
    
print (f"\nO total de alunos de tads é {qtd_tads}\nA média das notas dos {qtd} alunos é de {media:>2f}\nA {acima_media} alunos acima da média")


"""
 Faça um programa em Python que solicite ao usuário, enquanto o mesmo 
 desejar, números e armazene-os em uma lista.

 Após a entrada de dados, somar os valores da lista, calcular e mostrar a
 média.

 Calcule e mostre quantos números armazenados na lista estão acima da média.
"""

nums = []
continuar = 's'

while continuar.lower() == 's':
    num = float(input("Digite um número: "))
    nums.append(num)
    continuar = input("Deseja continuar inserindo números? (s/n) ")

soma_total = 0
acima_media = 0

for num in nums:
    soma_total += num

media = soma_total / len(nums)

for n in nums:
    if n > media:  # Compara o número atual com a média
        acima_media += 1

print (f"A média dos valores digitados é igual a {media:>2f}, e a quantidade de números acima desta média é {acima_media}")


"""
Elabore um programa em Python que leia os salários de 10 trabalhadores 
de uma empresa e os armazene em uma lista. Após a entrada de dados, 
o programa deverá:

Calcular a média desses salários.

Determinar o maior dos salários desta empresa.

Contar os salários menores que R$850,00.

Exibir todos os resultados na tela.
"""

salarios = []
qtd = 10

for i in range(qtd):
    salario = float(input(f"Digite o sálario do {i+1}º trabalhador da empresa: R$"))
    salarios.append(salario)

soma_salario = 0
menores = 0

for salario in salarios:
    soma_salario += salario
    media = soma_salario / qtd

    if salario < 850:
        menores += 1

maior = max(salarios)
    
print(f"\nA média de sálario dos trabalhadores é de R${media:.2f}, o trabalhador que tem o maior sálario recebe R${maior} e a quantidade de trabalhadores que recebe menos de R$850,00 é de {menores} trabalhadores")
