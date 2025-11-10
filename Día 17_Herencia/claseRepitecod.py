##1. Clase hija que repite código (sin super())

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad  # 👈 Nuevo atributo agregado
        print("✔ Constructor Persona actualizado")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # 👎 Aquí estamos repitiendo código del padre
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print("✔ Constructor Estudiante ejecutado (sin super)")
        # Nota: No estamos inicializando 'ciudad' aquí

e1 = Estudiante("Bairon", 31, "Ingeniería")
print(e1.nombre, e1.edad, e1.carrera)
# print(e1.ciudad)  # Esto causará un error porque 'ciudad' no está definido en Estudiante

