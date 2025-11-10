lista = [104, 240, 130, 40, 5]
def analizar_lista(numeros):
    if not numeros:
        return None, None, 0
    mayor = max(numeros)
    menor = min(numeros)
    suma = sum(numeros)
    
    promedio = suma / len(numeros)
    cont=0

    for i in numeros:
        if i % 2==0:
            cont+=1

    return mayor, menor, cont, promedio

analizar_lista(lista)
mayor, menor, cantidad_pares, promedio = analizar_lista(lista)

print("El número mayor es:", mayor)
print("El número menor es:", menor)     
print("La cantidad de números pares es:", cantidad_pares)
print("El promedio es:", promedio)