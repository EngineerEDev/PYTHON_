### clase
class Persona:
    # atributos de clase
    especie = "Humano"

    ##atributos de instancia (propios de cada persona)
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        
##crear objetos(instancias) de la clase Persona
persona1 = Persona("Juan", 28, "Madrid")    
persona2 = Persona("Ana", 22, "Barcelona")
persona3 = Persona("Luis", 35, "Valencia")  
persona4 = Persona("Carlos", 30, "Sevilla")

##acceder a los atributos de los objetos
print(persona1.nombre)##Juan
print(persona2.edad)##22    
print(persona3.especie)##Humano


    