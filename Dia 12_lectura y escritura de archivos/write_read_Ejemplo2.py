import csv
## newline='' es para evitar líneas en blanco adicionales en algunos sistemas operativos al escribir archivos CSV.
with open("archivo3.csv", "w", newline='') as archivo3:
    escritor_csv = csv.writer(archivo3)
    escritor_csv.writerow(["Nombre", "Edad", "Ciudad"])
    escritor_csv.writerow(["Ana", 28, "Madrid"])
    escritor_csv.writerow(["Luis", 34, "Barcelona"])
    escritor_csv.writerow(["Marta", 22, "Valencia"])

#"w" es para escribir (crea un nuevo archivo o sobrescribe uno existente)
#"r" es para leer (abre un archivo existente para lectura)  
#"a" es para agregar (abre un archivo existente para agregar contenido al final)

with open("archivo3.csv", "r") as archivo3:
    lector_csv = csv.reader(archivo3)
    print("Contenido del archivo CSV:\n")
    for fila in lector_csv:
        print(fila)

