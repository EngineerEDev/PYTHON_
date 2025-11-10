def area_rectangulo(base, altura):
    return base * altura

input_base = float(input("Ingrese la base del rectángulo: "))
input_altura = float(input("Ingrese la altura del rectángulo: "))  
area = area_rectangulo(input_base, input_altura)
print(f"El área del rectángulo es: {area}")