#from typing import final

#desafio022

#nome = str(input('Digite o Nome Completo De Uma Pessoa:\n'))
#print("Nome em maiusculo:")
#print(nome.upper())
#print("Nome em minusculo:")
#print(nome.lower())

#print("tamanho do nome sem contar os espaços:")
#print(len(nome.replace(" ","")))

#rp =  nome.split()[0]
#second = nome.split()[1]
#print("tamanho do primeiro nome:")
#print(len(rp))

#print("tamanho do segundo nome:")
#print(len(second))

#desafio023

#numero = int(input("Digite um numero:"))

#m = numero / 1000
#resto = numero % 1000
#c = resto / 100
#resto = resto % 100
#d =  resto / 10
#resto = resto % 10
#u = resto
#resto = resto

#print(f"Esse numero possui  {int(u)} Unidade")
#print(f"Esse numero possui {int(d)} dezena")
#print(f"Esse numero possui {int(c)} centena")
#print(f"Esse numero possui {int(m)} milhar")


#desafio024

#cidade = str(input("Digite o nome de uma cidade:"))

#cidade2 = cidade.split()[0]

#if cidade2.upper() == "SANTO":
    #print("Essa cidade começa com o Nome SANTO")
#elif cidade2.lower() == "santo":
    #print("Essa cidade começa com o Nome SANTO")
#else:
    #print("Essa cidade não começa com o Nome SANTO")

#desafio025

#pessoa = str(input("Digite o nome de uma pessoa:"))


#if "SILVA" in pessoa.upper():
    #print("SILVA" in pessoa.upper())
#elif "silva" in pessoa.lower():
    #print("SILVA" in pessoa.lower())
#else:
    #print("Não existe a palavra SILVA nesse nome")

#desafio026

#frase = str(input("Digite uma frase:"))


#if "A" in frase.upper():
    #print("A letra A Aparece:",frase.upper().count("A"),"vezes")
    #print("Sua posição inicial é:",frase.upper().find("A"))
    #print("Sua ultima posição é:",frase.upper().rfind("A"))
#else:
    #print("Essa frase não possui a letra a ")

#desafio027

#nome = str(input("Digite o Nome completo de uma pessoa:"))
#nome = nome.split()
#second = ((len(nome))-1)
# ou second [-1] já pega diretamente a ultima posição
#print("O primeiro nome è: ",nome[0])
#print("O segundo nome é: ",nome[second])











