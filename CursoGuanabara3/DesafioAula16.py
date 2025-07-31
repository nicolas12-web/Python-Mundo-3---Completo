#lanche = ("hanburguer","suco","pizza","pudim")
#print(len(lanche))
#for cont in range (0,len(lanche)):
      #print(f"{cont}", end= "")
from operator import index

#desafio 72
#contagem = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezeseis","dezesete","dezoito","dezenove","vinte","")
#c = 0
#res = int(input("Digite um numero: de [0 até 20]:"))
#while True:
    #if res < 0:
        #res = int(input("Numero Incorreto: Digite Um numero de [0 até 20]:"))
    #else:
        #for c in range (0,res + 1):
        #if c == res:
           # print(contagem[res])
    #break

#desafio 73

#contagem = ("corintia","sao paulo","botafogo","chapecoense","real madri","boca junior","vasco","internacional","flamengo","santos","palmeiras","psg","chelse","master city","fluminence","gremio","brasil","argentina","frança","belgica","alemanha")


#print(f"Os 5 primeiros Colocados São:\n{contagem[0:5]} \n")
#print(f"Os ultimos 4 colocados da tabela são:\n{contagem[-4:]}\n")
#print(f"Os Times em ordem alfabetica são:\n{sorted(contagem)}\n")
#print(f"E o time do Chapecoense ficou na:\n{contagem.index("chapecoense")} colocação")

#desafio 74
#primeira forma

#from random import randint
#lista = []
#menor = 0
#maior = 0

#for c in range (0,5):
 #hg = randint(1,50)
 #lista.append(hg)
 #if c == 0:
    #menor = hg
    #maior = hg
 #if hg > maior:
   # maior = hg
 #elif hg < menor:
    #menor = hg

#tupla = tuple(lista)
#print(tupla)
#print(f"O maior Numero da Tupla é {maior}")
#print(f"O menor Numero da Tupla é {menor}")

# segunda forma de se fazer e a forma correta de se fazer :

#from random import randint

#tupla = tuple((randint(1,50)) for c in range (0,5))

#print(tupla)
#print("O Maior Numero Da Tupla é:",max(tupla))
#print(f"O Menor Numero Da Tupla é: {min(tupla)}")

#desafio 75
#quanto = 0
#n = 0

#tupla = tuple(int(input(f"Digite o {c + 1} Valor:")) for c in range (4))
#quanto = (tupla.count(9))


#pares = tuple(n for n in tupla if n % 2 == 0 )


#print(f"O Numero 9 apareceu {quanto} vezes ")
#print(f"Numero Par que estão dentro da tupla: {pares}")
#if 3 in tupla:
 #print(f"O Numero 3 apareceu na posição {tupla.index(3)}")

 #desafio 76

#print("="* 65)
#print( " " * 25  + "Lista De Preço"  )
#print("="* 65)
#tupla = ("lapis",2.50,"borracha",3.50,"papel",4.60,"celular",10.50,"tablet", 11.20)

#tuplacarc = tuple((c for c in tupla if isinstance(c,str)))
#tuplaint = tuple((c for c in tupla if isinstance(c, (int, float))))

#tamanho = len(tuplacarc)
#for c in  range (0,tamanho):
   #print(f"{tuplacarc[c]}", end="")
   #print("." * 50 +"R$", end="")
   #print(" " * 2 + f"{tuplaint[c]:.2f}")

#print("="* 65)

 #desafio 77

#tupla = ( "arroz" , "feijao" , "macarrao","lasanha ","batata","pizza","hanburguer")


#for palavra in tupla:
   #vogais = ()
   #for letra in palavra :
     #if letra.lower() in "aeiou":
     # vogais +=(letra,)
   #print(f"Na palavra {palavra}  tem as vogais  {vogais}")
