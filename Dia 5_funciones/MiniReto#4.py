


def calcular_promedio(lista_numeros):
    cont=0
    suma=0
    for i in lista_numeros:
        suma+=i
        cont+=1
    return suma/cont
# NO MODIFICAR - INICIO

numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)   
print("El promedio es:", promedio) 