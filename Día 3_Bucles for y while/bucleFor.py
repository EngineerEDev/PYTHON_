#palabras clave: break, continue.
## break detiene la ejecución del bucle.
## continue salta a la siguiente iteración del bucle.   

for i in range(6):
    ##cuando i vale 3, se detiene el bucle
    if i == 3:
        break
    print("vuelta", i)


for i in range(6):
    ##cuando i vale 3, se salta esa iteración
    if i % 2 == 0:
        continue #salta cuando i es par
    print("vuelta", i)