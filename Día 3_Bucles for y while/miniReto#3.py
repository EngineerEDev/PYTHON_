
print("hecho con el ciclo for")
n=int(input("ingresa un numero: "))
sumador1=0
for i in range(1,n+1): #range excluye el último número.
    sumador1+=i
print("la suma de los numeros del 1 al", n, "es:", sumador1)

print("hecho con el ciclo while")
n1=int(input("ingresa un numero: ")) 
sumador2=0
i2=0
while i2 <=n1:
    sumador2+=i2
    i2+=1
print("la suma de los numeros del 1 al", n1, "es:", sumador2)