#desafio28
#import random

#a = random.randint(1,5)

#b = int(input("Digite um numero de 1 a 5 e tente acertar o numero que o computador pensou:"))
#print(f"Numero que o computador pensou: {a}")
#if b == a:
    #print("voce acertou")
#else:
    #print("voce errou")

#desafio29

#velocidade = float(input("Digite a velocidade do seu carro em km:"))

#if velocidade > 80:
    #veloc_ultra = 7 * (velocidade - 80)
    #print(f"Voce foi multado e terá que pagar:R${veloc_ultra:.2f}")

#desafio30

#a = int(input("Digite Um Valor:"))

#if a / 2 == 0:
    #print("Esse Numero é par")
#else:
    #print("Esse Numero é impar")

#desafio31

#distancia = float(input("Digite a distancia dessa viagem em KM:"))

#if distancia <= 200:
    #menor = distancia * 0.50
    #print(f"O valor da passagem é de:{menor:.2f}")
#else:
    #maior = distancia * 0.45
    #print(f"O valor da passagem é de:{maior:.2f}")

#desafio32

#ano = int(input("Digite um ano para ver se ele é bissexto:"))

#if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :
    #print("esse ano é bissexto:")
#else:
    #print("esse ano não é bissexto")


#desafio33

#valora = int(input("Digite o Valor A:"))
#valorb = int(input("Digite o Valor B:"))
#valorc = int(input("Digite o Valor C:"))

#if valora > valorb and valora > valorc:
    #print("O valor A é o maior valor")
#elif valorb > valora and valorb > valorc:
    #print("O valor B é o maior valor")
#elif valorc > valora and valorc > valorb:
    #print("O valor C é o maior valor")
#else:
    #print("não há um valor maior")

#if valora < valorb and valora < valorc:
    #print("O valor A é o menor valor")
#elif valorb < valora and valorb < valorc:
    #print("O valor B é o menor valor")
#elif valorc < valorb and valorc < valora:
    #print("O valor C é o menor valor")
#else:
    #print("não há um valor menor")





#desafio34

#salario = float(input("Digite o sálario de um funcionario:"))

#if salario > 1250:
    #salario =  salario + (salario * 10) /100
   # print(f"O salario com o aumento do funcionario agora é de:{salario:.2f}")
#elif salario <= 1250:
    #salario= salario + (salario * 15)/100
    #print(f"O salario com o aumento do funcionario agora é de:{salario:.2f}")

#desafio34

#retaa = float(input("Digite o complimento da primeira reta:"))
#retab = float(input("Digite o complimento da segunda reta: "))
#retac = float(input("Digite o complimento da terceira reta:"))

#if (retaa + retab > retac) and (retab + retac > retaa)  and (retaa + retac > retab):
    #print("Essa figura pode ser um triangulo")
#else:
    #print("Essa figura não pode ser um triangulo")







