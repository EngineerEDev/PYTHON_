saldo=1000
def depositar(monto):
    global saldo
    saldo += monto
    print(f"Depósito realizado. Nuevo saldo: {saldo}")

def consultar_saldo():
    print(f"Saldo actual: {saldo}")

def retirar(monto):
    global saldo
    if monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Retiro realizado. Nuevo saldo: {saldo}")

retirar(200)
depositar(500)
consultar_saldo()