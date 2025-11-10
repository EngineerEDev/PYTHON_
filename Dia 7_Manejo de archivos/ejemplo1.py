## "r" read(leer, da error si no existe el archivo)
# "w" write(escribir, si no existe el archivo lo crea, si existe lo sobreescribe)
# "a" append(agregar, si no existe el archivo lo crea, si existe agrega contenido al final)
# "r+" read and write (leer y escribir, si no existe da error)  
##siempre cerrar el archivo al finalizar con .close() o usar with open(que lo cierra automaticamente)

###escribir en un archivo de texto####

with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Estamos aprendiendo manejo de archivos en Python.\n")
