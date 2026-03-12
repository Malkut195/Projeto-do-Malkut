# Programa para obter o IMC (Índice de Massa Corporal):

from time import sleep

#Coleta de dados:

print("Seja bem vindo ao sistema para descobrir seu IMC (Índice de Massa Corporal), para isso, preciso que me responda:\n")

sleep(5)

altura = float(input("altura [m]:  "))
peso = float(input("peso [kg]:  "))

#Obtenção do IMC:

imc = peso / altura ** 2 

#Aplicando a tabela:

if imc < 18.5:
    resp = "está abaixo do peso"
elif imc >= 18.5 and imc < 25:
    resp = "está com peso ideal"
elif imc in range(25, 30):
    resp = "está em sobrepeso"
elif imc in range(30, 35):
    resp = "está com obesidade grau 1"
elif imc in range(35, 40):
    resp = "está com obesidade grau 2"
elif imc >= 40:
    resp = "está com obesidade grau 3"

#Resposta do programa:

sleep(3)

print("Seu IMC é {:.1f}, por isso você {}.".format(imc, resp))