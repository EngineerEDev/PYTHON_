
#acceder a caracteres individuales en una cadena de texto
texto="Python" 
print(texto[0])# Imprime la primera letra   
print(texto[-1])# Imprime la última letra
print(texto[1:4])# Imprime desde la segunda letra hasta la cuarta letra

##Metodos de cadenas de texto
mensaje="Hola Mundo"
print(mensaje.lower())# Convierte a minúsculas  
print(mensaje.upper())# Convierte a mayúsculas
print(mensaje.replace("Mundo", "Python"))# Reemplaza "Mundo" por "Python"
print(mensaje.split(","))# Divide la cadena en una lista usando la coma como separador
print(mensaje.strip())# Elimina espacios en blanco al inicio y al final
print(mensaje.find("Mundo"))# Encuentra la posición de "Mundo"
print(mensaje.startswith("Hola"))# Verifica si la cadena empieza con "Hola" 
print(mensaje.endswith("!"))# Verifica si la cadena termina con "!"
print(mensaje.count("o"))# Cuenta cuántas veces aparece la letra "o"    
print(mensaje.isalpha())# Verifica si la cadena contiene solo letras
print(mensaje.isdigit())# Verifica si la cadena contiene solo dígitos

#buscar dentro de una cadena de texto
texto2="Me gusta programar en Python"
print("python" in texto2) # Verifica si "python" está en la cadena (sensible a mayúsculas) #True
print(texto2.find("programar")) # Encuentra la posición de "programar" en la cadena #9

#interpolacion de cadenas de texto
nombre="Bairon Sarmiento"
edad=31
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.") # Usando f-strings
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)) # Usando format()
print("Hola, mi nombre es %s y tengo %d años." % (nombre, edad)) # Usando el operador % 
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.") # Usando concatenación
#%s para cadenas, %d para enteros, %f para flotantes
#.nf para limitar a n decimales