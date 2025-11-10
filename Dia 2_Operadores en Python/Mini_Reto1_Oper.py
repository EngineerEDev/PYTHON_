num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
print("la Suma de los dos numeros que ingresaste es:", num1 + num2)
print("la Resta de los dos numeros que ingresaste es:", num1 - num2)
print("la Multiplicacion de los dos numeros que ingresaste es:", num1 * num2)
print("la Division de los dos numeros que ingresaste es:", num1 / num2) # División flotante
print(f"el numero {num1} es mayor que {num2} {num1>num2}")#valor de tipo boleano
print(f"el numero {num1} es menor que {num2} {num1<num2}") #valor de tipo boleano
print(f"el numero {num1} es igual que {num2} {num1==num2}") #valor de tipo boleano
print("Ambos numeros son pares")
if num1%2==0 and num2%2==0:
    print("True")
else:
    print("False")