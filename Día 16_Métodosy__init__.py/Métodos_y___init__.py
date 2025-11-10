## 1) el metodo __init__ es un metodo especial que se ejecuta automaticamente al crear una instancia de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # atributo de instancia
        self.edad = edad       # atributo de instancia


# Crear objetos (instancias) de la clase Persona
p1 = Persona("Bairon", 31)
p2 = Persona("Daniela", 28)


print(p1.nombre, p1.edad)  # -> Bairon 31
print(p2.nombre, p2.edad)  # -> Daniela 28

## 2) metodos de instancia
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):   # método de instancia
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


