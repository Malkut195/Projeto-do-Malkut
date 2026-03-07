from random import randint
from time import sleep 

#Preparações iniciais:

bet = int(input("Digite um número de 1 a 5 para sua aposta:\n\n"))

numero = randint(1 , 5)
n = 1

#Sistema de perpetuacão até o acerto:

while bet != numero:
    sleep(2)
    
    #Sátira ao acéfalo:
    
    if bet > 5:
        n = 0
        frase = "você é incapaz de participar de um jogo para humanos"
        resposta = input("você é:\n\na) Burro\nb) Dislexo\nc) Não alfabetizado\nd) Todas as alternativas \n\n")
        sleep (5)
        print ("\nResposta correta:\nTodas as alternativas.")
        break
    
    # Motor continuo:
    
    bet = int(input(f"\nTentativa número {n}: Não foi dessa vez, tente denovo:\n\n"))
    numero = randint(1 , 5)
    n += 1

#Parte do feedback:

if n == 1:
    frase = "de primeira!? Você está roubando"
elif n in range (2, 5):
    frase = "até que foi razoável"
elif n in range (5, 10):
    frase = "você é inimigo da probabilidade, colega"
elif n > 10:
    frase = "veja pelo lado bom, pelo menos você foi persistente"

# Resultado:

print(f"Jogo encerrado com {n} tentaiva(s), {frase}.")