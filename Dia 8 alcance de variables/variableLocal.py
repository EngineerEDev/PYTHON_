

def saludar():
    global mensaje
    mensaje = "Hola, mundo!"  # 'mensaje' es una variable local a esta función
    print(mensaje)

saludar()
print(mensaje)  
