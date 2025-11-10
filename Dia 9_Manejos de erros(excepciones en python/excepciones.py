###con try/except podemos manejar los errores que se puedan presentar en nuestro codigo
###y evitar que el programa se detenga abruptamente

try:
    numero1 = int(input("ingrese un numero: "))##lo que puede generar un error
    numero2 = int(input("ingrese otro numero: ")) ##lo que puede generar un error
    resultado = numero1 / numero2                  ##lo que puede generar un error
    print(f"el resultado es: {resultado}")    ##lo que puede generar un error


#except ZeroDivisionError: ##capturamos el error que se puede presentar
#    print("no se puede dividir entre cero")
except ValueError: ##capturamos el error que se puede presentar
    print("debe ingresar un numero valido")

except Exception as e: ##capturamos cualquier otro error que se pueda presentar
    print(f"se ha producido un error: {e}")


#finally: ##siempre se ejecuta al final, haya o no error
#    print("gracias por usar el programa")

finally: ##siempre se ejecuta al final, haya o no error
    print("gracias por usar el programa")