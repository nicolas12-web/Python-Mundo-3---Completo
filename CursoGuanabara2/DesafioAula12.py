#desafio36

#casa = float(input("Digite o valor da Casa:"))
#salarioC = float(input("Digite o sálario do Comprador da casa:"))
#anosap = int(input("Digite em quantos anos o senhor deseja pagar: "))

#parcela =   casa / (anosap * 12 )
#porcentagem = (salarioC * 30) /100

#if parcela > porcentagem:
    #print("O Emprestimo foi reprovado")
#else:
    #print("O Emprestimo foi aprovado")

#desafio37

#print("Digite \033[1;31;40m 1 \033[m para converter o numero para binario\n")
#print("Digite \033[1;30;45m 2 \033[m para converter o numero para octal\n")
#print("Digite \033[7;37;44m 3 \033[m para converter o numero para hexadecimal\n")

#numero = int(input("Digite O Numero:"))

#numero1 = int(input("Digite o numero que voce quer converter:"))

#binario = bin(numero1)[2:]
#octal = oct(numero1)[2:]
#hexadecimal = hex(numero1)[2:]

#if numero == 1:
    #print(f"{binario}")
#elif numero == 2:
    #print(f"{octal}")
#elif numero == 3:
    #print(f"{hexadecimal}")

#Desafio038

#primeiro = int(input("Digite o primeiro valor:"))
#segundo = int (input("Digite o segundo valor:"))

#if primeiro > segundo:
    #print(f"Esse valor é o maior {primeiro}")
#elif primeiro < segundo:
    #print(f"Esse valor é o maior {segundo}")
#elif primeiro == segundo:
    #print("os valores são iguais ")

#desafio039

#anonasc = int(input("Digite o ano que voce nasceu:"))

#from datetime import datetime
#data = datetime.now().year

#alistar = data - anonasc

#if alistar < 18:
    #print("Voce ainda vai se alistar")
#elif alistar == 18:
    #print("Esta na hora de voce se alistar")
#elif alistar > 18:
    #print("já passou da hora de voce se alistar ")

#desafio40

#nota1 = float(input("Digite a primeira nota do Aluno:"))
#nota2 = float(input("Digite a segunda nota do Aluno:"))

#media = (nota1+ nota2) / 2

#if media < 5:
    #print("REPROVADO")
#elif media > 5 and media < 6.9:
    #print("RECUPERAÇÂO")
#elif media == 7 or media > 7:
    #print("APROVADO")

#desafio41

#from datetime import datetime

#data = datetime.now().year

#anoidade = int(input("Digite o seu ano de nascimento:"))

#idade =  data - anoidade

#if idade <= 9:
    #print("MIRIM")
#elif idade > 9 and idade <= 14:
    #print("INFANTIL")
#elif idade > 14 and idade <= 19:
    #print("JUNIOR")
#elif idade == 20:
    #print("SENIOR")
#elif idade > 20 :
    #print("MASTER")

#desafio42

#ra = float(input("Digite o lado A do triangulo:"))
#rb = float (input("Digite o lado B do triangulo:"))
#rc = float (input("Digite o lado C do triangulo:"))

#if ra + rb > rc and ra + rc > rb and rb + rc > ra:
    #print("A figura é um triangulo\n")
    #if ra == rb and ra == rc:
        #print("é um triangulo Equilátero")
    #elif ra != rb and ra != rc:
        #print("é um triangulo escaleno")
    #elif ra == rb or ra == rc or rb == rc or rb == ra or rc == ra or rc == rb:
        #print("é um triangulo Isoceles")
#else:
    #print("A figura não é um triangulo")

#desafio043

#peso = float(input("Digite a seu peso:"))
#altura = float(input("Digite a sua altura:"))

#imc = peso / (altura ** 2)

#print(f"O seu imc é {imc:.1f}")

#if imc < 18.5:
    #print("ABAIXO DO PESO")
#elif imc == 18.5 or imc <= 25:
    #print("\033[1:30:45m PESO IDEAL \033[m")
#elif imc == 25 or imc <= 30:
    #print("SOBREPESO")
#elif imc == 30 or imc <= 40:
    #print("OBSIDADE")
#elif imc > 40:
    #print("OBSIDADE MÒRBIDA")

#desafio044


#produto = 20

#while True:

    #print("-----------------------------")
    #print("Escolha a forma de Pagamento\n")
    #print("1-Dinheiro/Cheque")
    #print("2-cartão")
    #print("3-2x no cartão")
    #print("4-3x ou mais no cartão")
    #print("-----------------------------")
    #escolha = int(input("Digite qual sua opção de pagamento:"))

    #if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
        #break


#if escolha == 1:
    #escolha1 = produto - (produto * 10) / 100
    #print(f"Voce vai pagar {escolha1:.2f}")
#elif escolha == 2:
    #escolha2 = produto - (produto * 5) / 100
    #print(f"Voce vai pagar {escolha2:.2f}")
#elif escolha == 3:
    #print(f"Voce vai pagar {produto}")
#elif escolha == 4:
    #escolha3 =   produto   + (produto * 20)/ 100

#produto

#Desafio045
#import random
#import emoji

#papel = (emoji.emojize("papel:raised_hand:",language='alias'))
#tesoura = (emoji.emojize("tesoura:victory_hand:",language='alias'))
#pedra =  (emoji.emojize("pedra:raised_fist:",language='alias'))

#jogo = [papel,tesoura,pedra]

#maquina = random.choice(jogo)

#print("ESCOLHA PEDRA PAPEL TESOURA\n")

#print(f"1-{papel} ")
#print(f"2-{tesoura} ")
#print(f"3-{pedra}\n")

#escolha = str(input("Escolha Pedra ,Papel ou Tesoura Digite um Numero:"))

#if escolha == "1":
    #escolha = papel
#elif escolha == "2":
    #escolha = tesoura
#elif escolha == "3":
    #escolha = pedra

#if maquina == papel and escolha == pedra:
    #print(f"Maquina escolheu {papel} \033[31mvoce perdeu\033[m")
#elif maquina == papel and escolha == tesoura:
    #print(f"Maquina escolheu {papel} \033[32mvoce ganhou\033[m")
#elif maquina == tesoura and escolha == papel:
    #print(f"Maquina escolheu {tesoura} \033[31mvoce perdeu\033[m")
#elif maquina == tesoura and escolha == pedra:
    #print(f"Maquina escolheu {tesoura} \033[32mvoce ganhou\033[m")
#elif maquina == pedra and escolha == tesoura:
    #print(f"Maquina escolheu {pedra} \033[31mvoce perdeu\033[m")
#elif maquina == pedra and escolha == papel:
    #print(f"Maquina escolheu {pedra} \033[32mvoce ganhou\033[m")
#elif maquina == pedra and escolha == pedra or maquina == papel and escolha == papel or maquina == tesoura and escolha == tesoura:
    #print(f"Maquina escolheu {escolha} \033[35mEMPATOU\033[m")






















