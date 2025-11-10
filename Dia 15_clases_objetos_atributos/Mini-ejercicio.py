

class vehiculo:

    ruedas = 4
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
#crear objetos(instancias) de la clase vehiculo
carr01 = vehiculo("Toyota", "Corolla", 2020)
carr02 = vehiculo("Honda", "Civic", 2019)
#acceder a los atributos de las instancias  
print(carr01.marca, carr01.modelo,carr01.año)##Toyota
print(carr02.marca, carr02.modelo,carr02.año)##Honda

##acceder a los atributos de la clase
print(carr01.ruedas,carr02.ruedas)##4
vehiculo.ruedas = 6 ##modificar el atributo de clase
print(carr01.ruedas,carr02.ruedas)##6
carr01.ruedas = 8 ##crear un atributo de instancia con el mismo nombre que el atributo de clase
print(carr01.ruedas,carr02.ruedas)##8 6


