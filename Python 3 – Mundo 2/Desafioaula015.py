# desafio 66
#c = 0
#soma = 0
#while True:
   #a = int(input("Digite Um numero:  para Sair Digite[999]:"))
   #if a == 999:
        #break
   #c += 1
   #soma += a

#print(f" Foram Digitados: {c}")
#print(f" A Soma dos Numeros é: {soma}")

# desafio 67

#c = 1
#r = 0
#while True:
    #print("=" * 30)
    #print("           TABUADA     ")
    #print("=" * 30)
    #t = int(input("Digite Qual Tabuada Voce Quer Ver:"))
    #if t < 0:
        #break
    #else:
      #while c != 11:
       #r = t * c
       #print(f"{t} X {c} = {r}")
       #c += 1
    #c = 1

# desafio 68
#import random
#c = 0

#while True:
 #maquina = random.randint(1,10)
 #print("=" * 30)
 #print("Vamos brincar de impar ou par:")
 #print("="*30)
 #a = int(input("Digite Um Numero de [1 a 10]:"))
 #b = str(input("Digite[impar ou par]:")).strip().upper()[0]
 #c = maquina + a
 #print("\n")
 #if b == "I" and c % 2 == 1:
     #print("VOCE GANHOU DA MAQUINA")
     #print(f"A MAQUINA ESCOLHEU O NUMERO {maquina} ")
     #print(f" {a} + {maquina} = {c} E {c} É UM NUMERO IMPAR")
 #elif b == "P" and c % 2 == 0:
     #print("VOCE GANHOU DA MAQUINA")
     #print(f"A MAQUINA ESCOLHEU O NUMERO {maquina} ")
     #print(f"{a} + {maquina} = {c} E {c} É UM NUMERO PAR")
 #elif b == "I" and c % 2 != 1:
    #print("VOCE PERDEU PARA A MAQUINA")
    #print(f"A MAQUINA ESCOLHEU O NUMERO {maquina} ")
    #print(f"{a} + {maquina} = {c} E {c} É UM NUMERO PAR")
    #break
 #elif b == "P" and c % 2 != 0:
    #print("VOCE PERDEU PARA A MAQUINA")
    #print(f"A MAQUINA ESCOLHEU O NUMERO {maquina} ")
    #print(f"{a} + {maquina} = {c} E {c} É UM NUMERO IMPAR")
    #break

#desafio 69
#m18 = 0
#hcad = 0
#m20 = 0
#sim = "nenhum"
#while True:
    #id = int(input("Digite a Idade:"))
    #sexo = str(input("Qual o Sexo [F/M]:")).strip().upper()[0]
    #if id > 18:
        #m18 += 1
    #if sexo  == "M":
        #hcad += 1
    #elif sexo == "F" and id < 20:
        #m20 += 1
    #sim = str(input("Deseja Continuar:[S/N]")).strip().upper()[0]
    #if sim == "N":
        #break

#print(f"Quantidade de pessoas com mais de 18 anos:{m18}")
#print(f"A Quantidade De Homens è:{hcad}")
#print(f"Quantidade de Mulher Com Menos de 20 anos de idade: {m20}")

# desafio 70

#gasto = 0
#c = 1
#mais1000 = 0
#nomeb = "nenhum"
#primeiro = 0

#while True:
    #nome = str(input("Digite o Nome do Produto:"))
    #preco = float(input("Digite o Preço do produto:"))
    #gasto += preco
    #if preco > 1000:
        #mais1000 += 1
    #if c == 1:
     #primeiro = preco
     #c +=1
    #if primeiro > preco:
        #nomeb = nome
        #primeiro = preco
    #continua = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    #if continua == "N":
        #break
#print(f"O total de Gasto é : {gasto:.2f}")
#print(f"{mais1000} Produto Custa mais de 1000 reais")
#print(f"O Nome Do produto Mais Barato é {nomeb}")

# desafio 71

#valors =  int(input("Digite o valor quer voce quer sacar:"))

#  primeira maneira
#nota100 = 0
#nota50 = 0
#nota20 = 0
#nota10 = 0
#nota1 = 0
#resto100 = 0
#resto50 = 0
#resto20 = 0
#resto10 = 0


#nota100 = valors // 100
#resto100 =  valors % 100
#if resto100 != 0:
 #nota50 = resto100 // 50
 #resto50 =  resto100 % 50
#if resto50 != 0:
 #nota20 = resto50 // 20
 #resto20 =  resto50 % 20
#if resto20 != 0:
 #nota10 = resto20 // 10
 #resto10 = resto20 % 100
#if resto10 != 0:
 #nota1 = resto10

#print("="*20)
#if nota100 != 0:
 #print(f"{nota100:.0f} Notas de 100")
#if nota50!= 0:
 #print(f"{nota50:.0f} Notas de 50")
#if nota20 != 0:
 #print(f"{nota20:.0f} Notas de 20")
#if nota10 != 0:
 #print(f"{nota10:.0f} Notas de 10")
#if nota1 != 0:
 #print(f"{nota1:.0f} Notas de 1")
#print("="*20)

#segunda maneira e uma melhor maneira

#valor = int(input("Digite O Valor que deseja Sacar:"))
#valor1 = valor
#retira = 100
#cnota = 0

#while True:
    #if valor1 >= retira:
        #valor1 -= retira
        #cnota += 1
    #else:
        #if cnota != 0:
         #print(f"A quantidade de nota de {retira} é de {cnota} cédulas")
        #cnota = 0
        #if valor1 == 0:
            #break
        #if valor1 != 0:
          #if retira == 100:
              #retira = 50
          #elif retira == 50:
              #retira = 20
          #elif retira == 20:
              #retira = 10
          #elif retira == 10:
              #retira = 1


























