
#from time import sleep
#pessoas = {"humano": "nicolas", "filmes": "jarvascripto"}

#for k,v in pessoas.items():
    #sleep(1)
    #print(f" o {k} chama {v}")}

#desafio 90

#di = {}
#ne = []

#di['Nome:'] = input("Digite um Nome:")
#di['Nota:'] =  float(input("Digite uma nota:"))

#ne.append(di.copy())

#if ne[0]['Nota:'] < 5:
    #print(f"O {ne[0]['Nome:']} Reprovou ")
#else:
    #print(f"O {ne[0]['Nome:']} Está Aprovado")

#desafio 91

#gg = {}
#c = 0
#d = []
#totgol = 0
#gg['Nome'] = input("Digite um Nome:")
#gg['Partida'] = int(input(f"Quantas Partidas {gg['Nome']} jogou :"))

#for i in range(gg['Partida']):
    #ggg = int(input(f"Quantos Gols Na Partida {c + 1}:"))
    #totgol += ggg
    #d.append(ggg)
    #ggg = 0
    #c += 1
#gg['Gols'] = d.copy()
#print(f"O Jogador {gg['Nome']} Jogou {c} Partidas")
#c -= c
#for i in range(gg['Partida']):
    #print(f"Na Partida {c + 1} , {gg['Nome']}  fez {gg['Gols'][i]} Gols")
    #c += 1
#print(f"O Numero Total de Gols Foi {totgol}")

#desafio 92
#from datetime import date

#di = {}
#lista = []
#ano = 0
#nasc = 0
#apos = 0
#ano1 = 0
#di['Nome'] = input("Digite o Nome:")
#nasc =  int(input("Digite o Ano de nascimento:"))
#ano =  date.today().year
#ano1 = ano - nasc
#di['Idade'] = ano1
#di['Cart'] = int(input("Digite sua carteira de trabalho[não tem Digite 0]:"))
#di['Contrato'] = int(input("Digite o Ano em que voce foi Contratado:"))
#di['Salario'] = float(input('Digite O Seu Salario:'))
#apos = ano - di['Contrato']
#apos = 35 - apos
#apos = ano1 + apos
#di['aposentadoria'] = apos
#lista.append(di.copy())

#print(lista)
#print()
#for ii in lista:
    #for k,e in ii.items():
        #print(f"{k} tem o valor {e}")
    #print()

# desafio 93
from random import randint

#dicionario = {}
#lista = []
#jogado = 0
#listaaux = []
#c = 0

#while True:
    #jogado = randint(1,10)
    #while jogado in listaaux:
            #jogado = randint(1, 10)
    #print(f"O Jogador {c + 1} Tirou {jogado}")
    #lista.append(f"Jogador {c + 1} Tirou {jogado}")
    #listaaux.append(jogado)
    #if c == 3:
        #break
    #c += 1
#c = 0
#dicionario['kk'] = lista
#print()
#print("Ranking Dos Jogadores")

##dicionario['kk'].sort(key=lambda s: int(s.split()[-1]) ,reverse = True)
#c = 0
#for c , numero in  enumerate(dicionario['kk']):
        #print(f'o {c + 1}º lugar foi {numero}')
#desafio 94
#dici = {}
#lista = []
#Listaw  = []
#acimam = []
#cm = 0
#qtd =  int(input("Digite a quantidade de pessoas que deseja cadastrar:"))
#c = 0
#id = 0
#medi = 0
#for i in range(qtd):
    #dici['Nome'] = input('Digite um Nome:')
    #dici['Sexo'] = input("Digite o Sexo Da Pessoa:")
    #if dici['Sexo'].lower() == "f":
     #cm += 1
     #Listaw.append(dici['Nome'])
    #dici['Idade'] = int(input(f"Digite a idade de {dici['Nome']}:"))
    #id += dici['Idade']
    #lista.append(dici.copy())
    #c += 1
    #dici.clear()
    #print()

#media
#medi =  id / c
#print(f"Foram Cadastradas {c} pessoas")
#print(f"A Media de Idade Foi De {medi:.1f}")
#print(f"Foi cadastrada(s)  {cm} mulher(s) , Nome : {Listaw}")

#for i in lista:
    #if i['Idade'] > medi:
       # acimam.append(i['Nome'])


#print(f"As Pessoas Com Idade Acima Da Media São : {acimam}")

#desafio 95

#dici = {}
#lista = []
#tot = 0
#tot1 = []
#soma = []
#soma2 = []
#ccc = 0
#while True:
  #dici['Nome'] = input("Digite O Nome Do Jogador:")
  #dici['Qtd'] = int(input(f"Quantas Partidas {dici['Nome']} jogou:"))
  #for i in range(dici['Qtd']):
      #dici['Gols'] = int(input(f"Quantos Gols Na Partida {i + 1}:"))
      #tot += dici['Gols']
      #soma.append(dici['Gols'])
  #lista.append(dici.copy())
  #soma2.append(soma.copy())
  #tot1.append(tot)
  #tot = 0
  #soma.clear()
  #continua = input("Quer Continuar ? [S/N]:")
  #if continua.lower() == "s":
      #print("-" * 30)
  #elif continua.lower() == "n":
      #print("-=" * 20)
      #break

#print("Cod Nome", " " * 6, "Gols", " " * 6,"Total" )
#print("-" * 40)
#for o,j in enumerate(lista):
    #print(f"{o + 1}   {j['Nome']} ", " " * 6 ,f"{soma2[o]}", " " * 6, f"{tot1[o]}" )

#print()
#while True:
   # nome1 = int(input("Mostrar Dados De Qual Jogador Ou [-1] Para Sair:"))
    #if nome1 == -1:
          # break
    #print(f"-- LEVANTAMENTO DO JOGADOR  {lista[nome1 - 1 ]['Nome']}:")
    #for ii in (soma2):
       # for ll in ii:
           # print(f"No Jogo {ccc + 1} fez {ll} Gols")
           # ccc += 1





