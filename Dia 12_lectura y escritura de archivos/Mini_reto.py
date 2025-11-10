

def agregar_usuario(nombre):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(nombre + "\n")

def imprimir_usuarios():
    with open("usuarios.txt", "r") as archivo:
            usuarios = archivo.readlines()##.readlines() lee todas las lineas del archivo y las guarda en una lista
            print("Usuarios registrados:")
            for usuario in usuarios:
                print(usuario.strip())##.strip() elimina los espacios en blanco al inicio y al final de una cadena

while True:
    

    try:
        print("\nOpciones:")
        print("1. Agregar usuario")
        print("2. imprimir usuarios")
        print("3. Salir")
        name=int(input("ingrese una opcion (1-3) "))
        if name == 1:
         agregar_usuario(input("ingrese el nombre del usuario: "))
        elif name == 2:
         imprimir_usuarios()
        elif name == 3:
         print("saliendo del programa")
         break
    except ValueError:
        print("debe ingresar un numero valido")
    
  
