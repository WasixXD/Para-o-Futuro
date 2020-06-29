def main():
    for c in range(5):
        lista.append(randint(1,10))
    print(f"Sorteando {len(lista)} valores aleatorios: ", end="")
    
    for c in lista:
        print(c, end=" ", flush=True)
        sleep(1)
    print() 
                
def soma(lista):
    par = 0
    for c in lista:
        if c % 2== 0:
            par += c
    print(f"Somando os valores pares de {lista} temos o valor {par}")
    

    
main()       
soma(lista)
#Simples mas foi o centésimo
