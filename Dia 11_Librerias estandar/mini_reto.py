from math import sqrt,factorial
from random import randint
from datetime import datetime
from os import getcwd
num=int(input("Ingrese un numero: "))


fecha_actual=datetime.now()
fecha_actual=fecha_actual.strftime("%d/%m/%Y (hora: %H:%M:%S)") #formatea la fecha
print(f"hoy es: {fecha_actual}")

num_aleatroio=randint(1,100)

print(f"el numero aleatorio entre 1 y 100 es : {num_aleatroio}")
print(f"numero ingresado es: {num}")
print(f"la raiz cuadrada es: {sqrt(num)}")
print(f"factorial es: {factorial(num)}")

print(f"Directorio actual: {getcwd()}") 