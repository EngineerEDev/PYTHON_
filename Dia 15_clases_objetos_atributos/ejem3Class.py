class persona:

    especie = "Humano" ##atributo de clase (compartido por todas las instancias)
    def __init__(self, nombre, edad):
        #atributos de instancia (propios de cada instancia)
        self.nombre = nombre
        self.edad = edad

a= persona("Juan", 28)
b= persona("dani", 22)
print(a.nombre)##Juan
print(b.edad)##22   
print(a.especie)##Humano
print(b.especie)##Humano


print(a.__dict__)  ##{'nombre': 'Juan', 'edad': 28}
print(b.__dict__)  ##{'nombre': 'dani', 'edad': 22

print(persona.__dict__) ##muestra los atributos de la clase
##__dict__ es un atributo especial que contiene un diccionario con los atributos de la instancia o clase
