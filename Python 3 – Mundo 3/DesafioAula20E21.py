



#def fun(nomee):
    #print('-' * 30)
    #print(nomee)
    #print('-' * 30)

#fun(" Meu Nome é Nicolas")
#fun("Primeiro Codigo Versionado")
#fun("Primeira Atividade Com Função")



#def soma(x,y):
    #print(f" A Soma de {x} + {y} é = ", end="")
    #kk = x + y
    #print(kk)

#Programa Principal
#soma(1,2)
#soma(3,4)
#soma(5,6)

#empacotamento com função


#def dobra(listaa):
  #cc = len(listaa)
  #for cont in range(cc):
    #listaa[cont] = 2 * listaa[cont]
    #cont += 1
  


#lista = [2,4,6,8,9]
#dobra(lista)
#print(lista)


#Desafio 96

#def area(x,y):
    #u = 0
    #u = x * y
    #print(f"A Area do seu Terreno de {x}X{y} é  de :{u}")


#a = float(input("Digite a aréa do terreno:"))
#b = float(input("Digite o comprimento do terreno:"))
#area(a,b)



#Desafio 97

#def adpt (n):
    #o = len(n)
    #print('-' * o )
    #print(f"{n}")
    #print('-' * o )
    #print(o)


#adpt("Ola, Mundo")
#adpt("meu nome é guanabara")
#adpt("eu tenho 2 anos ")


#Desafio 98
#from time import sleep
#def fun(a,b,c):
    #for i in range (1,11):
        #sleep(0.2)
        #print(f"{i}" , end = " ",flush=True)
    #print(" FIM")
    #print()
    #for j in range (10,-2,-2):
        #sleep(0.2)
       # print(f"{j}", end=" ",flush=True)
    #print(" FIM")
    #print()
    #for h in range(a,b + 1,c):
        #sleep(0.2)
        #print(f"{h}", end=" ",flush=True) 
    #print(" FIM")


#a =  int(input("Digite o Inicio:"))
#b =  int(input("Digite o Final:"))
#c =  int(input("Digite os Passo: "))
#print()
#fun(a,b,c)


#Desafio 99
#def a1(*s):
 #y  = 0
 #y = max(*s)
 #print(f"O maior Valor é : {y}")


#a1(1,4,6)

#a1(4,8,10)


#ou 


#def a2(*r):
    #y =  r[0]
    #for i in r:
        #if i > y:
           # y = i 
    #print(y)

#a2(2,6,8,5,4)
#a2(9,8,10,3,2)





#Desafio 100

#def sorteia():
 #from random import randint
 #listaa = []
 #a = 0
 #for i in range (5):
     #while a in listaa:
       # a = randint(1,10) 
     #listaa.append(a)
 #return listaa


#def Somapar(a):
   #e = 0
   #for i in a:
      #if i % 2 == 0:
         #e += i 
  # return e


#codigo principal 

#numero  =  sorteia()
#kk = Somapar(numero)
#print(numero)
#print(kk)


#Desafio 101





#from datetime import date 

#def voto(a=0,b=0):
    #e = 0
    #e = b - a 
    #if e < 18:
        #print(f"Com {e} O Voto  é NEGADO voce ainda não possui a idade necessaria")
    #elif e >= 18 and e < 65:
        #print(f"Com {e} O Voto é OBRIGATORIO")
    #elif e >= 65:
        #print(f"Com {e} O Voto é OPCIONAL")



 
#ano = int(input("Digite O Ano Do Seu Nascimento:"))
#data = date.today().year
#voto(ano,data)

#Desafio 102


#def fatorial(a,show=True):
    #y = a
    #c = 0
    #d = a - 1 
    #if show == True:
        #for i in range(a):
             #c = d * a
             #a = c 
             #if d != 0:
                #print(f"{y} X {d} = {c}")
                #d -= 1 
    #else :
        #for j in range(a): 
          #if d != 0: 
            #c =  a * d
            #a = c  
          #d -= 1
        #print(f"O Fatorial De {y} é {c}") 

#a = int(input("Voce quer ver o Fatorial De Qual Numero?"))
#fatorial(a,False)



#Desafio 103

#def ficha (a=0,b=0):
    #if a == "":
       # a = "<Desconhecido>"
    #if b == 0 or b == "":
        #b = 0
    #print(f"O Jogador {a} Marcou {b} Gols")


#nome = input("Digite o Nome Do Jogador:")
#Gols = input("Digite a Quantidade de Gols Que o Jogador Marcou:")
#print()
#ficha(nome,Gols)

#Desafio 104


def leiaint(a):
  b = 0
  while True:
    try:
        b = int(input(a))
        return b
    except ValueError:
       print("Erro Digite Novamente")
   


a = leiaint("Digite Um Numero:")
print(f"O Numero que Voce Digitou Foi O Numero {a}")



# Desafio 105

#def notas(a, sit=True):
    #"""
   # Nessa função pegamos o maior numero
   # o menor numero 
    #a media 
    #"""
    #aa = 0
    #rr ={}
    #rr['tamanho'] = len(a)
    #tamanhoo = len(a)
    #rr['maior'] =  max(a)
    #rr['menor'] = min(a)
    #for i in dici:
        #aa += i
    #rr['media'] = aa / tamanhoo
    #if sit:
        #if rr['media'] < 5:
           # rr['Situacao'] = "Ruim"
        #elif rr['media']  > 5:
           # rr['Situacao'] = "Boa"
        #elif rr['media'] ==  5:
            #rr['Situacao'] = "media"
    #return rr
    

#dici = {1,2,3,4,5,6,7,8,9}
#dici = {5,4,4,4}
#dici = {7,8,9,10}
#kkk = notas(dici)
#print(kkk)

# Desafio 106

#a = "a"

#while a.lower() != "fim":
    #print("~" * 30)
    #print("\033[1;35;40m  Sistema De Ajuda pyHELP \033[m")
    #print("~" * 30)

    #a = (input("Digite Uma Função Ou Biblioteca:"))
    #if a.lower()!= "Fim":
       # help(a)
        


