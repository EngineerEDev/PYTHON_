"""with open("notas.txt", "r") as notas:
    contenido = notas.readlines()
    print(contenido)
    for linea in contenido:
        print(linea.strip())

    print("Número de líneas:", len(contenido))
"""

with open("notas.txt", "r") as notas:
    lineas = notas.readlines()
    for i, linea in enumerate(lineas, start=1):
        print(f"Línea {i}: {linea.strip()}") 
    print("Número de líneas:", len(lineas))   