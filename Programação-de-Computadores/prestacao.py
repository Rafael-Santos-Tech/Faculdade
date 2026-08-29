# Exercicio 4
vprestacao = float(input("Digite o valor da prestação a ser paga:R$ "))
multa = float(input("Digite qual é a porcentagem de multa paga por dia: "))
dias = int(input("DIgite quantos dias de atraso: "))
prestacao = vprestacao  + (vprestacao * (multa / 100) * dias)
print ("A prestação a ser paga vai ser de R$%.2f após %s dias" % (prestacao,dias))