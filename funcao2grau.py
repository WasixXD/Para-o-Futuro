import math
a = int(input("Digite seu A: "))
if a > 0:
    concavidade = "CIMA"
else:
    concavidade = "BAIXO"

b = int(input("Digite seu B: "))

c = int(input("Digite seu C: "))



print(" ")
print("Sua funcão ficou assim: {}x²{}x{}".format(a, b, c))
resposta = str(input("Certo?: ")).upper()
print(" ")

while resposta != "SIM":
    print("Então coloque novamente os números:")
    print(" ")
    a = int(input("Digite seu A: "))
    if a > 0:
        concavidade = "CIMA"
    else:
        concavidade = "BAIXO"

    b = int(input("Digite seu B: "))
    c = int(input("Digite seu C: "))
    resposta = str(input("Certo?: ")).upper()

if b > 0:
    delta = b**2 -4*a*c
else:
    delta = (b)**2 -4*a*c

raiz = delta**(1/2)
xlinha = (-b + raiz)/(2*a)
xdlinha = (-b - raiz)/(2*a)

verticep = -b/(2*a)
vertices = -delta/(4*a)



print(" ")
print("A concavidade será para {}".format(concavidade))
print("O eixo y será cortado no {}".format(c))
print("O eixo x cortará nos pontos {:.1f} e {:.1f}".format(xlinha, xdlinha))
print("A vertice cortará respectivamente em {}, {}".format(verticep, vertices))
print("D(f)= R")
