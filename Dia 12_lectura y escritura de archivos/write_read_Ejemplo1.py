##escritura de un archivo
with open("archivo2.txt","w",) as archivo2:
    archivo2.write("Hola, este es un archivo de texto.\n")
    archivo2.write("Estamos aprendiendo a leer y escribir archivos en Python.\n")
    archivo2.write("¡Es muy divertido!\n")

##lectura de un archivo
with open("archivo2.txt","r") as archivo2:
    contenido = archivo2.read()
    print("Contenido del archivo:\n")
    print(contenido)

#"w" es para escribir (crea un nuevo archivo o sobrescribe uno existente)
#"r" es para leer (abre un archivo existente para lectura)  
#"a" es para agregar (abre un archivo existente para agregar contenido al final)

#with open(...) as ...: es una forma segura de manejar archivos, ya que asegura que el archivo se cierre correctamente después de su uso, incluso si ocurre un error durante la operación.  
