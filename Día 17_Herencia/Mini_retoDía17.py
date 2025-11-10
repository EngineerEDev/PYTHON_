# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("✔ Constructor Persona ejecutado")

    def mostrar_info(self):
        print(f"👤 Nombre: {self.nombre}, Edad: {self.edad}")


# Clase intermedia que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # llama al constructor de Persona
        self.salario = salario
        print("✔ Constructor Empleado ejecutado")

    def mostrar_info(self):
        super().mostrar_info()  # reutiliza método de Persona
        print(f"💰 Salario: {self.salario}")


# Clase hija que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)  # llama al constructor de Empleado
        self.departamento = departamento
        print("✔ Constructor Gerente ejecutado")

    def mostrar_info(self):
        super().mostrar_info()  # reutiliza método de Empleado
        print(f"🏢 Departamento: {self.departamento}")


# --- Probando ---
p = Persona("Ana", 30)
print("\nPersona:")
p.mostrar_info()

e = Empleado("Luis", 28, 2500)
print("\nEmpleado:")
e.mostrar_info()

g = Gerente("Bairon", 31, 5000, "Tecnología")
print("\nGerente:")
g.mostrar_info()
