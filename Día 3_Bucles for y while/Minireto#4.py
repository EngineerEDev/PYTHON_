n=int(input("ingresa un numero: "))
contador=0
i=1
while i <=n:
    if i%2==0:
        print(i)
        contador+=1
    i+=1
print("la cantidad de numeros pares del 1 al", n, "es:", contador)
    