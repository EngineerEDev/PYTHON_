class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        print("✔ Constructor Persona actualizado")

class Estudiante(Persona):
    def __init__(self, nombre, edad, ciudad, carrera):
        super().__init__(nombre, edad, ciudad)  # ✅ reutiliza al padre
        self.carrera = carrera
        print("✔ Constructor Estudiante ejecutado (con super)")

e2 = Estudiante("Daniela", 28, "Bogotá", "Contaduría")
print(e2.nombre, e2.edad, e2.ciudad, e2.carrera)
# Ahora 'ciudad' está correctamente inicializado en Estudiante 