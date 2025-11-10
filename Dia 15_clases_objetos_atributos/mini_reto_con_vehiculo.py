class Vehiculo:
    ruedas = 4  # atributo de clase

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


# Lista para guardar los vehículos creados
vehiculos = []

while True:
    print("\n--- MENÚ DE VEHÍCULOS ---")
    print("1. Agregar vehículo")
    print("2. Mostrar vehículos")
    print("3. Cambiar número de ruedas (atributo de clase)")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción (1-4): "))

        if opcion == 1:
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            año = int(input("Ingrese el año: "))
            vehiculo = Vehiculo(marca, modelo, año)
            vehiculos.append(vehiculo)
            print("✅ Vehículo agregado con éxito.")

        elif opcion == 2:
            if not vehiculos:
                print("❌ No hay vehículos registrados.")
            else:
                print("\nLista de vehículos:")
                for i, v in enumerate(vehiculos, start=1):
                    print(f"{i}. {v.marca} {v.modelo} ({v.año}) - Ruedas: {v.ruedas}")

        elif opcion == 3:
            nuevo_valor = int(input("Ingrese el nuevo número de ruedas para TODOS los vehículos: "))
            Vehiculo.ruedas = nuevo_valor
            print(f"✅ Se cambió el número de ruedas a {Vehiculo.ruedas} para todos los vehículos.")

        elif opcion == 4:
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida.")

    except ValueError:
        print("⚠️ Debe ingresar un número válido.")
