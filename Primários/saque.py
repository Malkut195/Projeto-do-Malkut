#Saque pelo caixa eletrônico 

from time import sleep

#Coleta de informacões:

nome = str(input("Digite o seu nome completo:\n\n")).strip().title()

p_nome = nome.split()[0]
u_nome = nome.split()[-1]

senha = str(input(f"\nPor favor, Sr(a). {p_nome} {u_nome}, digite seu PIN de 4 digitos:\n\n")).strip()

#Testando senha do usuário:

saque = 0
x = 0

for x in range(0, 3):
    
    if senha == "1234":
        saque = int(input("\n\033[32mDigite o valor que deseja sacar:\033[m\n\n"))
        
        while saque <= 0:
            
            print("\n\033[31mValor incompatível.\033[m")
            saque = int(input("\nPor favor, digite um valor compatível:\n\n"))
        break
    
    else:
        
        sleep(1)
        
        print(f"\n\033[31mSENHA INCORRETA\n\nVocê possui mais {(2 - x)} tentativas:\033[m")
        
        senha = str(input("\n"))                
        
        if x == 2:
            print("\n\033[31;1mTentativas esgotadas, cartão bloqueado.\033[m")
            exit()         
        x += 1       

#Efetuando o saque do cliente.

print(f"\nContabilizando o saque de {saque} reais...")

sleep(5)

lst = [50, 10, 1]
resp = []

for n in range(0, 3):
    c = saque // int(lst[n])
    r = saque % int(lst[n])
    resp.append(c)
    saque = r
    
#Mostrando a resposta ao usuário.

print(f"\nSeu saque será de:\n\n{resp[0]} cédulas de cinquenta.\n{resp[1]} cédulas de dez.\n{resp[2]} moedas de um real.")