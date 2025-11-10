#listas (list)
#son colecciones de datos ordenadas y mutables. Permiten elementos duplicados.
#se definen con corchetes []
numeros=[10,20,30,40]
nombres=["Ana","Luis","Pedro"]

print(numeros[0]) #acceder al primer elemento
numeros.append(50) #agregar un elemento al final
numeros[1]=25 #modificar el segundo elemento
print(numeros) #imprimir la lista completa

#tuplas (tuple)
#son colecciones de datos ordenadas e inmutables. Permiten elementos duplicados.
#se definen con paréntesis ()
coordenadas=(5,10)
print(coordenadas[0]) #acceder al primer elemento --> 5
#coordenadas[0]=15 #esto generaría un error porque las tuplas son inmutables


#diccionarios (dict)
#son colecciones de datos desordenadas, mutables y no permiten elementos duplicados.    
#se definen con llaves {}
#son pares clave-valor
persona = {"nombre":"Bairon",
        "edad":31,
        "Programador":True }
print(persona["nombre"]) #acceder al valor asociado a la clave "nombre"
persona["edad"]=32 #modificar el valor asociado a la clave "edad"   
persona["Programador"]=False #modificar el valor asociado a la clave "Programador"

print(persona) #imprimir el diccionario completo
persona["ciudad"]="Santa Marta" #agregar una nueva clave-valor
