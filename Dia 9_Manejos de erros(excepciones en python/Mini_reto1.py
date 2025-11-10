
try:
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese otro numero: "))
    dev= num1/num2
    print(f"El resultado es: {dev}")
except ZeroDivisionError:
    print("No se puede dividir entre cero") 
except ValueError:
    print("Debe ingresar un numero valido")

