saldo=1000
def depositar(monto):
    global saldo
    saldo += monto
    print(f"Depósito realizado. Nuevo saldo: {saldo}")

def consultar_saldo():
    print(f"Saldo actual: {saldo}")


depositar(500)
consultar_saldo()