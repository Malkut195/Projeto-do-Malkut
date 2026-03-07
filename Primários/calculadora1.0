from time import sleep

txt = str(input("Digite sua operação abaixo:\n(+ ; - ; . ; / ; ^ ; √)\n\n")).strip()
print("\n")
print("-" * 48)
print("\nCalculando...\n")

sleep(3)

lst = txt.split()

n1 = int(lst[0])
n2 = int(lst[2])

opr = lst[1]

if opr == "+":
    rsp = n1 + n2
elif opr == "-":
    rsp = n1 - n2
elif opr == ".":
    rsp = n1 * n2
elif opr == "/":
    if n2 == 0:
        print ("ERRO: divisão por zero.")
        rsp = 0
    else: 
        rsp = n1 / n2        
elif opr == "^":
    rsp =  n1 ** n2
elif opr == "√":
    rsp = n1 ** (1/n2)
else:
    print("ERRO: sinal não indentificado.")
    rsp = 0

print ("Resposta:   {:.2f}".format(rsp))