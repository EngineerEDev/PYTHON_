##1. Importar un módulo
import math

print(math.sqrt(16))  # raíz cuadrada
print(math.pi)        # constante pi

##2. Importar funciones específicas de un módulo
from math import sqrt, pi   
print(sqrt(25))  # raíz cuadrada

##3. Importar un módulo con un alias
import math as m
print(m.sqrt(36))  # raíz cuadrada
print(m.pi)        # constante pi

##4. Crear y usar un módulo personalizado
# Supongamos que tenemos un archivo llamado mi_modulo.py con el siguiente contenido:    
