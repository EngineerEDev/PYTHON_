
def num_positivo(numx):
    if numx < 0:
        raise Exception("❌ No se puede calcular raíz de negativos.")
    return True

try:
    num = int(input("Ingrese un número: "))

    if num_positivo(num):
        raiz = num ** 0.5
        print(f"La raíz cuadrada de {num} es: {raiz}")


except ValueError:
    print("❌ Debes ingresar un número válido.")

except Exception as e:
    print(e)
finally:
    print("Gracias por usar el programa")