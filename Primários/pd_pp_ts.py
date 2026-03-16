#Pedra, papel, tesoura

from time import sleep
from random import choice
import matplotlib.pyplot as plt

#Emolduração do jogo:

input("Para jogar, saiba que:\n\npd = pedra\npp = papel\nts = tesoura\n\nSaiba que deve digitar 'f' para dar fim ao jogo. Precione 'enter' para começar.\n\n")

hp = []
hc = []
he = []
pp = 0
pc = 0
tempo = []
t = 0
empates = 0

while True:
    
    jp = input("\nSua jogada:\n\n").lower().strip()
    jc = choice(["pd", "pp", "ts"])
    
    sleep(1)
    
    if jp == "f":
        break
                
    if jp not in ["pd", "pp", "ts"]:
        print("Comando inválido!")
        continue
    
    print(f"\n{jc}")
    
    tempo.append(t)
    t += 1
    
    hp.append(pp)
    hc.append(pc)
    he.append(empates)
    
    if jc == jp:
        empates += 1
        continue
    
    elif jp == "pd":
        
        if jc == "pp":
            pc += 1
            
        elif jc == "ts":
            pp += 1
    
    elif jp == "pp":
        
        if jc == "pd":
            pp += 1
            
        elif jc == "ts":
            pc += 1
            
    elif jp == "ts":
        
        if jc == "pd":
            pc += 1
        elif jc == "pp":
            pp += 1
            
#Exibição do resultado do jogo:

if pp > pc:
    resp = "\033[32;1mvenceu\033[m"
elif pc == pp:
    resp = "empatou.."
else:
    resp = "\033[31;1mperdeu\033[m"


if t > 0:
    
    plt.plot(tempo, hp, label="Você", color='green', marker='o')
    plt.plot(tempo, hc, label="Bot", color='red', marker='x')
    plt.plot(tempo, he, label="Empates", color='gray', marker='s')
    
    
    plt.title("Placar")
    plt.xlabel("Rodadas")
    plt.ylabel("Pontos")
    plt.legend()
    plt.grid(True)
    
    print(f"\nJogo encerrado, você {resp}.")
    
    plt.show()

else: 
    print("\n\033[1;31mVocê precisava ter jogar ao menos uma vez.\033[m")