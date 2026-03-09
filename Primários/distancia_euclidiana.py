#Introdução à proposta:

print("Esse programa te informará a distância entre dois pontos em um plano cartesiano.\n\nPara isso, peço que me informe no modelo 'x y' sem parenteses nem vírgula.\n")

#Coleta de informações:

x1_y1 = input("Digite a posição cartesiana do ponto um:\n\n").strip()
x2_y2 = input("\nDigite a posição cartesiana do ponto dois:\n\n").strip()

#Organização da informacão:

x1 = float(x1_y1.split()[0])
y1 = float(x1_y1.split()[1])
x2 = float(x2_y2.split()[0])
y2 = float(x2_y2.split()[1])
dx = abs(x1 - x2) ** 2
dy = abs(y1 - y2) ** 2
ds = (dx + dy) ** 1/2

#Resposta:

print(f"\nA distância entre os dois pontos é {ds:.2f}.")