## en python se tienen varios tipos de datos
# enteros la palabra reservada es int
# decimales la palabra reservada es float
# cadenas de texto la palabra reservada es str
# booleanos la palabra reservada es bool

edad = 25 # int
estatura = 1.75 # float 
nombre = "bairon" # str
es_programador = True # bool

print(f"la variable edad tiene un contipo de dato:  {type(edad).__name__}")
print(f"la variable estatura contiene un tipo de dato :{type(estatura).__name__}")
print(f"la variable nombre contiene un tipo de dato: {type(nombre).__name__}")
print(f"la variable es_programador contiene un tipo de dato: {type(es_programador).__name__}")
# para conocer el tipo de dato se usa la funcion type()