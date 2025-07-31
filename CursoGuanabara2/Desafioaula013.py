
#desafio 46
#import time
#import emoji

#print("Contagem regresiva para fogos de Artificios:")
#for i  in range (10,-1,-1):
    #print(f"{i}")
    #time.sleep(1)
#print(emoji.emojize("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥"))


#desafio 47

#for i in range (1,51):
    #if i % 2 == 0:
        #print(f"{i}")

#desafio 48
#soma = 0
#for i in range (1,501):
    #if i % 2 == 1 and i % 3 == 0:
        #soma += i
#print(f"{soma}")

#desafio49
#number = int(input("Digite um numéro de 1 até 10:"))

#for i in range(1,11):
    #d = number * i
    #print(f"{number} X {i} = {d}")
    #d = 0

#desafio50
#soma = 0
#for i in range(1,7):
    #number = int(input(f"Digite o {i} numero:"))
    #if number % 2 == 0:
        #soma += number
#print(f"O resultado da soma é:{soma}")

#desafio51

#termo1 = int(input("Digite o Primeiro termo da PA:"))
#razao = int(input("Digite a razão dessa PA:"))

#for i in range(0,10):
   #print(f"{termo1}")
   #termo1 = termo1 + razao

#desafio52

#number = int(input("Digite um numero para ver se ele é um numero primo:"))
#kk = 0
#for i in range (1,number + 1,1):
    #if number % i == 0:
      #  print(f"\033[32m {i}\033[m")
      #  kk += 1
    #else:
       # print(f"\033[31m {i}\033[m")


#if kk == 2 :
    #print(f"{number} é um numero primo!!")
#else:
    #print(f"{number} não é um numéro primo!!")

#desafio : pratica String
#nome = str(input("Digite uma frase para descobrirmos se é uma frase palindromo:"))
#nome1 = nome.split()
#pedaco = nome1[1][:3]
#print(f"{pedaco}")

#desafio 53

#letra = str(input("Digite uma frase para vermos se ela é  um polindromo:"))
#letra = letra.replace(" " ,"")

#letra2 =  letra[::-1]

#if letra == letra2:
    #print("essa palavra é um polindromo")
#else:
    #print("Essa palavra não é um polindromo")


#desafio54
#from _datetime import datetime

#anonow = datetime.now().year

#menor = 0
#maior = 0

#for i in range(1,8):
    #anop = int(input(f"Digite o ano de nascimento da {i} pessoa:"))
    #if anonow - anop < 18:
       # menor = menor + 1
    #else:
       # maior = maior + 1

#print(f"{menor} não atingiram a maior idade:")
#print(f"{maior} atingiram a maior idade:")



#desafio55

#maior = 0
#menor = 0

#vet = []

#for i in range (1,6):
    #peso = float(input(f"Digite o peso da {i} pessoa:"))
    #vet.append(peso)
#maior = vet[0]
#menor = vet[0]

#for i in range (1,5):
    #if vet[i] > maior:
        #maior = vet[i]
    #else:
        #menor = vet[i]

#print (f"O maior valor Digitado foi: {maior:.1f}")
#print(f"O menor valor Digitado foi: {menor:.1f}")


#maior = 0
#menor = 0

#inicio = float(input("Digite a 1 posição:"))

#menor = inicio
#maior = inicio

#for i in range (2,6):
    #number = float(input(f"Digite a  {i} posição:"))
    #if number > maior:
        #maior = number
    #elif number < menor:
        #menor = number

#print(f"O maior numéro é o: {maior}")
#print(f"O menor numéro é o: {menor}")

#desafio56

#maior = 0
#menor = 999
#media = 0
#nomem = "nenhum"
#menos20 = 0

#for i in range(1,5):
    #nome = str(input(f"Digite a nome da {i} pessoa:"))
    #idade = int(input(f"Digite a idade da {i} pessoa:"))
    #sexo = str(input(f"Digite o sexo [f/m] da  {i}  pessoa:"))
    #media += idade
    #if idade > maior and sexo.lower() == "m":
       # maior = idade
        #nomem = nome
    #if idade < 20 and sexo.lower() == "f":
        #menos20 += 1

#media = media / 4

#print(f' A media da idade desses 4 são:{media:.1f}')
#print(f" O nome do homem mais velho é {nomem} e sua idade é {maior} anos:")
#print(f" Há {menos20} mulheres com menos de 20 anos:")


#desafio 57
#Nome = "nenhum"
#while True:
    #Nome = str(input("Digite o sexo:"))
    #if Nome.upper() == "M":
        #break;
    #elif Nome.upper() == "F":
        #break
    #else:
        #print("Digite novamente se é F ou M:")
#segunda maneira de fazer
#Nome = "nenhum"
#while Nome.upper()  != "M" and Nome.upper() != "F":
     #Nome = str(input("Digite o sexo:"))
     #if Nome.upper()!= "M" and Nome.upper()!= "F":
         #print("Digite novamente se é F ou M:")


#desafio 58

#import random

#computer = 0
#advinha = 1

#while advinha != computer:
 #computer = random.randint(1 ,10)
 #advinha = int(input("Advinhe o numero que o computador está pensando:"))
 #if advinha == computer:
     #print(f"Voce acertou o numero que a maquina pensou: {computer}")
 #else :
     #print(f"a maquina pensou: {computer}")
     #print("Voce errou, tente novamente \n")

#desafio 59
#N=0
#soma = 0
#mult = 0
#maior = 0

#a = int(input("Digite o primeiro numero:"))
#b = int(input("Digite o segundo numero:"))

#while N != 5:

 #print("=======================")
 #print("""DIGITE UM DOS NUMEROS  """)
 #print("=======================")
 #print("[1] SOMAR")
 #print("[2] MULTIPLICAR")
 #print("[3] MAIOR")
 #print("[4] NOVOS NUMEROS")
 #print("[5] SAIR DO PROGRAMA")
 #print("=======================")

 #N = int (input(""))
 #if N == 1:
     #soma = a + b
     #print(f"A Soma Desses 2 numeros é: {soma}\n")
 #elif N == 2:
     #mult = a * b
     #print(f"A multiplicação desses 2 numeros é : {mult}\n")
 #elif N == 3:
     #if a > b:
         #print(f"O Maior Numero è: {a}\n")
     #else:
         #print(f"O Maior Numero è: {b}")
 #elif N == 4:
     #a = int(input("Digite o primeiro numero:"))
     #b = int(input("Digite o segundo numero:"))
 #elif N == 5:
    #break

#desafio 60

#n1 = 0
#arm = 0

#n1 = int(input("Digite um valor:"))
#n = n1
#n2 = n1
#if n1 == 0:
   # arm = 1 ;
#else:
 #while n != 1:
    #n -= 1
    #arm = n2 * n
    #if n != 0:
     # n2 = arm
#print(f"O fatorial de {n1} é: {arm}")

#segunda maneira
#arm = 0
#n2 = 0

#n1 = int(input("Digite um valor:"))
#n2 = n1
#n = n1
#if n2 == 0:
    #print(f"O fatorial de n1 é {n1}")
#else:
   # while True:
        #n -= 1
        #arm = n2 * n
        #if n != 1:
         #n2 = arm
        #elif n == 1:
           # break

#print(f"O fatorial de {n1} é: {arm}")

#desafio 61

#a = int (input("Digite o primeiro termo da sua PA:"))
#b = int (input("Digite a razao da sua PA:"))

#c = 10
#while c != 0:
    #c -= 1
    #print(f"{a}")
    #a = a + b


#desafio 62

#a = int (input("Digite o primeiro termo da sua PA:"))
#b = int (input("Digite a razao da sua PA:"))

#c = 10
#while True:
    #print(f"{a}->", end="")
    #c -= 1
    #if c == 0:
       # break
    #a = a + b
#print("\n")
#while True:
   # kk = int(input("Digite 1 para continuar Ou 0 para sair:"))
    #if kk == 0:
     #print("Fim do programa!!")
     #break
   # elif kk ==  1:
    # kkl = int(input(f"Quantos termos a mais voce quer ver após {a}:"))
    # c =kkl
     #while c != 0:
       #  a = a + b
        # print(f"{a}->", end="")
       #  c -= 1
   # print("\n")

#desafio 63

#a = int (input(f"Digite até  Qual posição voce quer ver na sequencia de Fibonacci:"))
#zero = 0
#um = 1
#guarda = 0
#c = 0
#if a == 2:
    #print(f"{zero},{um}")
#while c != a - 2 :
    #if a <= 0:
        #break
    #elif a == 1:
        #print(f"{zero}")
        #break
    #if zero == 0:
     #print(f"{zero},{um}", end=",")
    #guarda = zero + um
    #print(f"{guarda}", end=",")
    #zero = um
    #um = guarda

    #c += 1


#desafio 64
#c = 0
#soma = 0
#i = 0

#while i != 999:
    #i = int(input("Digite um numero:"))
    #if i != 999:
      #c += 1
      #soma += i

#print(f"Foram Digitados {c} numeros")
#print(f"A Soma desses numeros foi de {soma}")

#desafio 65

#media = 0
#menor = 0
#maior = 0
#mant = 0
#c = 0
#while True:
    #valor = int(input("Digite um valor:"))
    #mant += valor
    #c += 1
    #if mant == valor:
        #maior = valor
        #menor = valor
    #elif valor > maior:
        #maior = valor
    #elif valor < menor:
       # menor = valor
    #a = str(input("Deseja continuar:[S/N]:"))
    #if a.upper() == "N":
        #break


#media = mant / c
#print(f"O Menor valor foi {menor}")
#print(f"O Maior valor foi {maior}")
#print(f"A Media Foi:{media:.1f}")

#maior = 0
#menor = 0

#for i in range(1,6):
    #a = int(input(f"Digite o {i} numero:"))
    #if i == 1:
       # maior = a
        #menor = a
    #elif a > maior:
       # maior = a
    #elif a < menor:
       # menor = a

#print(f"O Maior Numero foi {maior}")
#print(f"O menor Numero foi {menor}")



































