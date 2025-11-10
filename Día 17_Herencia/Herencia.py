##herencia
class animales:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def hacer_sonido(self):
        print("El animal hace un sonido")

class perro(animales):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Guau Guau")

class gato(animales):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Miau Miau")

g=gato("Michi")
p=perro("Firulais")
g.hacer_sonido()
p.hacer_sonido()
