#Atividade 78
# primeira forma de fazer

#lista = []
#menor = 0
#maior = 0
#posicaom = 1
#posicaomm = 1
#for c in range (0,5):
    #lista.append(int(input(f"Digite O {c + 1} Valor Da Lista:")))
    #if c == 0:
        #maior = lista[0]
        #menor = lista [0]
    #if lista[c] > maior:
        #maior = lista[c]
        #posicaom = c + 1
    #if lista[c] < menor:
        #menor  = lista[c]
        #posicaomm = c + 1

#print(f" O Maior Numero foi {maior}  e sua posição é : {posicaom}")
#print(f" O Menor Numero foi  {menor}  e sua posição é : {posicaomm}")

#segunda forma de fazer

#lista = []
#menor = 0
#maior = 0
#posicaom = 1
#posicaomm = 1

#for a in range(0,5):
    #lista.append(int(input(f"Digite O {a + 1} Valor Da Lista:")))

#for v,c in enumerate(lista):
    #if v == 0:
        #maior = lista[v]
        #menor = lista [v]
    #if lista[v] > maior:
        #maior = lista[v]
        #posicaom = v + 1
    #if lista[v] < menor:
        #menor  = lista[v]
        #posicaomm = v + 1

#print(f" O Maior Numero Foi {maior}  e sua posição é : {posicaom}")
#print(f" O Menor Numero Foi  {menor}  e sua posição é : {posicaomm}")

#Atividade 79

#lista = []

#while True:
    #kkl = (int(input(f"Digite um valor de[0/20] se quiser sair digite [-1]:")))
    #if kkl == -1:
        #break
    #if kkl not in lista:
        #lista.append(kkl)

#lista = sorted(lista)

#for c in lista:
 #print(f"{c}")

 #atividade 80
#lista = []
#v =  0
#for c in range (0,5):
 #valor = (int(input(f"Digite o [{c+1}] numero , ou Digite [-1] para sair:")))
 #if valor == -1:
     #break
 #if c == 0:
  #v = valor
  #lista.append(valor)
 #if v < valor:
   #lista.append(valor)
   #v = valor
 #if v > valor:
     #lista.insert(0,valor)
     #v =  valor

#for i in lista:
    #print(f"{i}")

#atividade 81

#lista = []
#c = 0

#while True:
    #numero = int(input("Digite um numero , ou para sair Digite [-1]:"))
    #if numero == -1:
        #break
    #lista.append(numero)
    #c += 1
#print("\n")
#print(f"Foram Digitados {c} numeros \n")
#lista = sorted((lista),reverse = True)
#print(f"A Ordem decrescente é :")
#for i in lista:
   #print(f"{i}", end = "->")
#print("Fim\n")
#if 5 in lista:
    #print("O Valor 5 está na lista")
#else :
    #print("O valor 5 não está na lista")

#atividade 82

#lista = []
#listai = []
#listap = []

#while True:
    #numero = (int(input("Digite um Numero , Ou Digite [-1] para sair:")))
    #if numero == -1:
        #break
    #lista.append(numero)

#for i in lista:
    #if i % 2 == 0:
        #listap.append(i)
    #else:
        #listai.append(i)

#print(lista)
#print(listap)
#print(listai)

#atividade 83
#a = 0
#b = 0
#while True:
    #letra = (str(input("Digite uma expressão para verificarmos , Ou [n] para sair:")))
    #if letra.lower() == "n":
        #break
        #a  = cont.letra(")")
        #b  = cont.letra("(")
    #if "(" in letra  and ")" in letra  and a == b:
        #print("Sua expressão está correta!!")
    #else:
       # print("Sua expressão não está correta")

#atividade84

#lista = list()
#dado = list()
#cc = 0
#maior = 0
#menor = 0
#nomep = []
#nomel = []
#while True:
    #dado.append(str(input("Digite Um Nome Ou  N para sair :")))
    #if dado[0] in "Nn":
        #break
    #dado.append(float(input("Digite o Peso:")))
    #lista.append(dado[:])
    #cc += 1

    #dado.clear()

#print("\n")
#for c in range (len(lista)):
    #print(f"{lista[c][0]} tem {lista[c][1]:.1f} Killos")

#print("\n")

#if lista and len(lista[0]) > 0:
 #if isinstance(lista[0][1],(int,float)) and lista[0][1] > 0:
  #print(f"Foram cadastradas {cc} Pessoas")
  #for i in range(len(lista)):
      #if i == 0:
        #maior =  lista[i][1]
        #menor = lista[i][1]
        #nomep.append(lista[i][0])
        #nomel.append(lista[i][0])
      #else:
         #if lista[i][1] > maior:
             #maior = lista[i][1]
             #nomep.clear()
             #nomep.append(lista[i][0][:])
         #elif lista[i][1] == maior:
             #maior = lista[i][1]
             #nomep.append(lista[i][0][:])
         #if lista[i][1] < menor:
           #menor = lista[i][1]
           #nomel.clear()
           #nomel.append(lista[i][0][:])
         #elif lista[i][1] == menor:
            # menor = lista[i][1]
             #nomel.append(lista[i][0][:])
#if nomel == nomep:
    #print("Não há nem maior nem menor os pesos são iguais")
#else:
 #if lista and len(lista[0]) > 0:
  #if isinstance(lista[0][1],(int,float)) and lista[0][1] > 0:
   #print(f"maior peso : {nomep} ")
   #print(f"menor peso : {nomel}")

#desafio 85

#parimpar = [[],[]]
#var = 0

#for i in range (0,7):

 #var = int(input(f"Digite o {i + 1 } Valor:"))
 #if var % 2 == 0:
     #parimpar[0].append(var)
 #elif var % 2 == 1:
     #parimpar[1].append(var)

#parimpar[0].sort()
#parimpar[1].sort()
#print(f"Os numéros impares  foram \n {parimpar[1]}\n")
#print(f"Os numéros pares foram \n {parimpar[0]}\n")

#desafio 86

#matriz = []
#linha = []
#valor = 0
#for i in range (3):
    #linha = []
    #for c in range (3):
        #valor = int(input(f"Digite o numero da matriz da posição [{i}] [{c}]: "))
        #linha.append(valor)
    #matriz.append(linha)

#for linha in matriz:
     #for d in linha:
         #print(f"[{d}]",end="")
     #print()

#desafio 87

#matriz = []
#linha = []
#valor = 0
#pares =  0
#somat = 0
#maior = 0
#for i in range (3):
    #linha = []
    #for c in range (3):
        #valor = int(input(f"Digite a posição [{i}] [{c}]:"))
        #if valor % 2 == 0:
            #pares += valor
        #if c == 2:
            #somat += valor
        #if i == 1:
           #maior = valor
        #if i == 1:
            #if valor > maior:
                #maior = valor

        #linha.append(valor)
    #matriz.append(linha)

#for linha in matriz:
     #for d in linha:
         #print(f"[{d}]",end="")
     #print()

#print(f"A soma dos valores pares é {pares}")
#print(f"A soma dos valores da terceira coluna é: {somat}")
#print(f"O maior valor da segunda linha é {maior}")

#desafio 88
#from random import randint
#matriz = []
#linha = []

#print("="*35)
#print(9*" ","JOGO DA MEGA SENA")
#print("="*35)

#nu =  int(input("Quantos Jogos Voce Quer que eu Sorteie?"))
#print()
#print(f"-=-=-=-=-= SORTEANDO {nu} JOGOS -=-=-=-=-=-=")
#for i in range(nu):
    #linha = []
    #for c in range (6):
       #n = randint(1,60)
       #while n == linha:
         #n = randint(1, 60)
       #linha.append(n)
    #matriz.append(linha)
#for c,i in enumerate (matriz[2:],start=2):
    #print(f"Jogo {c + 1}:", end = "")
    #for j in i:
        #print(f"[{j}]", end = "")
    #print()

#desafio 89

#matriz = []
#media = []
#nota0 = []
#mede = 0
#while True:
    #lista = []
    #nota = []
    #media1 = []
    #nome = str(input("Digite o Nome do Aluno:"))
    #nota1 = float(input(f"Digite a Primeira Nota De {nome}:"))
    #nota2 = float(input(f"Digite a Segunda Nota De {nome}:"))
    #nota.append(nota1)
    #nota.append(nota2)
    #nota0.append(nota[:])
    #mede = (nota1 + nota2) / 2
    #media1.append(mede)
    #media.append(media1[:])
    #lista.append(nome)
    #lista.append(nota1)
    #lista.append(nota2)
    #matriz.append(lista[:])
    #continuar = str(input("Deseja continuar [S/N]:"))
    #if continuar.lower() == "n":
        #break

#print("-=" * 20)
#print("N", 5 * " " , "NOME" ,5 * " " ,"MEDIA")
#print("-" * 40)
#for c, aluno in enumerate(matriz):
       #print(f"{c + 1}", 5 * " " ,aluno[0] ,5 * " ",f"{media[c][0]:.1f}")
#print("-" * 40)


#while True:
 #fi = int(input("Mostrar notas de qual aluno:(999 interrompe):"))
 #if fi == 999:
    #break
 #if fi <= len(matriz) and fi > 0:
   #print(f"As Notas de {matriz[fi - 1][0]}  foram {nota0[fi - 1 ][0]} e {nota0[fi - 1 ][1]}")
 #else :
   #print("Aluno Não encontrado")













