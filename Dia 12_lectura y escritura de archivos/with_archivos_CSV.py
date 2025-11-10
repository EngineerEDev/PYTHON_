"""
nombre,edad,ciudad
Juan,28,Madrid
Ana,22,Barcelona
Luis,35,Valencia
"""

import csv
def agregar_usuario(nombre, edad, ciudad):
    with open("usuarios.csv", "a",newline="") as archivo: ##newline="" evita lineas en blanco al escribir en CSV
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, edad, ciudad])##.writerow escribe una fila en el archivo CSV

def imprimir_usuarios():
    with open("usuarios.csv", "r") as archivo:
            lector = csv.reader(archivo)##.reader lee el archivo CSV y lo convierte en un objeto iterable
            print("Usuarios registrados:")
            for fila in lector:
                print(f"Nombre: {fila[0]}, Edad: {fila[1]}, Ciudad: {fila[2]}")##acceder a los elementos de la fila por su indice


agregar_usuario("Carlos", 30, "Sevilla")
agregar_usuario("Marta", 25, "Bilbao")
agregar_usuario("Sofia", 29, "Granada")
imprimir_usuarios()
