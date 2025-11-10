saldo=1000
def depositar(monto):
    global saldo
    if monto <= 0:   # 👈 Validación
        print("⚠️ El monto a depositar debe ser mayor que 0.")
        return
    saldo += monto
    print(f"Depósito realizado. Nuevo saldo: {saldo}")

def consultar_saldo():
    print(f"Saldo actual: {saldo}")

def retirar(monto):
    global saldo
    if monto > saldo:
        print("Fondos insuficientes.")
    if monto <= 0:   # 👈 Validación
        print("⚠️ El monto a retirar debe ser mayor que 0.")
        return
    else:
        saldo -= monto
        print(f"Retiro realizado. Nuevo saldo: {saldo}")




while True:
    print("\nOpciones:")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        consultar_saldo()
    elif opcion == '2':
        monto = float(input("Ingrese el monto a depositar: "))
        depositar(monto)
    elif opcion == '3':
        monto = float(input("Ingrese el monto a retirar: "))
        retirar(monto)
    elif opcion == '4':
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")


