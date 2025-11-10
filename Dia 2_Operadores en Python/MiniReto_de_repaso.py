num=int(input("Ingrese un numero: "))
if num > 0:
    if num % 2 == 0:
        print("El numero es positivo y par, ")
        print("su raiz cuadrada es:", num**0.5,"su cadrado es:", num**2)
    else:
        print("El numero es positivo e impar")
        print("su raiz cuadrada es:", num**0.5,"su cadrado es:", num**2)
elif num < 0:
    if num % 2 == 0:
        print("El numero es negativo y par")
        print("su raiz cuadrada es:", num**0.5,"su cadrado es:", num**2)
    else:
        print("El numero es negativo e impar")
        print("su raiz cuadrada es:", num**0.5,"su cadrado es:", num**2)
else:
    print("El numero es cero y es par")
###otra forma de hacerlo
import math

num = int(input("Ingrese un número: "))

# Calcular cuadrado y raíz (usamos valor absoluto para raíz si es negativo)
cuadrado = num ** 2
raiz = math.sqrt(abs(num))

if num > 0:
    print("El número es positivo", end=", ")
elif num < 0:
    print("El número es negativo", end=", ")
else:
    print("El número es cero (y par)")
    
if num != 0:  # solo evaluamos par/impar si no es cero
    if num % 2 == 0:
        print("y par.")
    else:
        print("e impar.")

print("Su cuadrado es:", cuadrado)
print("Su raíz cuadrada (valor absoluto):", raiz)
# --- IGNORE ---
# --- IGNORE ---