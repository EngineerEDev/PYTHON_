
oracion=input("Ingrese una oracion: ")
print(oracion[:3])#imprime los primeros 2 caracteres
print(oracion[-3:])#imprime los ultimos 3 caracteres


print(oracion)
oracion_sin_vocales=oracion
for i in "aeiouAEIOU":
    oracion_sin_vocales=oracion_sin_vocales.replace(i,"*") 
print(oracion_sin_vocales)

posicion=oracion.find("Python")

# posicion de la palabra python}
posicion=oracion.find("python")
print("Posición de la palabra 'Python':", posicion)
#5 frase invertida
frase_invertida=oracion[::-1]
print("Frase invertida:", frase_invertida)