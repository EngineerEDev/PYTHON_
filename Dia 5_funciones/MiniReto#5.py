def numero_mayor(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    
    return lista[-1]

    


print("El numero mayor es:", numero_mayor(3, 5, 2))