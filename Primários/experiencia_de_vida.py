a = int(input("Quantos anos você tem? "))
b = int(input("Quer viver quantos anos? "))
c = a * 365 + (a // 4)
d = (a / b) * 100
g = (b - a) * 365 / 7
if b >= 80:
    print("Quanta esperança...")
print("Tu já viveste {} dias na sua vida... parece muito, né!?".format(c))
print("Aliás, você já experienciou {:.0f}% da sua existência... passou, não tem volta, colega.".format(d))
print("Veja pelo lado bom, você ainda vai viver mais {:.0f} longas segundas-feiras. Aproveite-as pois essa cruel porcentagem ({:.0f}%) só vai aumentar.".format(g, d))
