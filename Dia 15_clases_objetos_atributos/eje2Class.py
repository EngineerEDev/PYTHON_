##clase vacia y atributos dinamicos
class Persona:  ##clase vacia (un molde para crear objetos)
    pass ##indica que no hace nada, se usa para definir clases o funciones vacias

objeto1 = Persona()##crear un objeto(instancia) de la clase Persona
objeto2 = Persona()##crear otro objeto(instancia) de la clase Persona   
##agregar atributos(de instancia) dinamicos a los objetos
objeto1.nombre = "Juan"
objeto1.edad = 28
objeto1.ciudad = "Madrid"   
objeto2.nombre = "dani"
objeto2.edad = 22       
objeto2.ciudad = "Barcelona"

print(objeto1.nombre)##Juan
print(objeto2.edad)##22 
print(objeto1.ciudad)##Madrid
print(objeto2.nombre)##dani
print(type(objeto1))##<class '__main__.Persona'>
