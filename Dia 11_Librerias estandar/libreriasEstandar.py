##semana n°2 Dia 11
#Librerias estandar de python
#https://docs.python.org/3/library/

#Libreria Math
import math 
print(math.sqrt(16)) #raiz cuadrada
print(math.pi)#numero pi
print(math.e)#numero e
print(math.pow(2,3)) #2 elevado a la 3     
print(math.factorial(5))#factorial de 5
print(math.log(100,10)) #logaritmo en base 10 de 100    
print(math.sin(90)) #seno de 90 grados
print(math.cos(0)) #coseno de 0 grados
print(math.tan(45)) #tangente de 45 grados
print(math.ceil(4.2)) #redondea hacia arriba
print(math.floor(4.7)) #redondea hacia abajo

#Libreria Random
import random
print(random.randint(1,10)) #numero aleatorio entre 1 y 10  
print(random.choice(['rojo','verde','azul'])) #elige un elemento aleatorio de la lista
print(random.random()) #numero aleatorio entre 0 y 1    
print(random.uniform(1,10)) #numero aleatorio entre 1 y 10 con decimales
lista = [1,2,3,4,5] 
random.shuffle(lista) #mezcla los elementos de la lista
print(lista)
print(random.sample(lista,3)) #elige 3 elementos aleatorios de la lista


#Libreria Datetime trabaja con fechas y horas
import datetime
fecha_actual = datetime.datetime.now() #fecha y hora actual 
print(fecha_actual)
print(fecha_actual.year) #año actual
print(fecha_actual.month) #mes actual
print(fecha_actual.day) #dia actual 
print(fecha_actual.hour) #hora actual
print(fecha_actual.minute) #minuto actual
print(fecha_actual.second) #segundo actual
fecha_especifica = datetime.datetime(2020,5,17) #fecha especifica   
print(fecha_especifica)
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S") #formatea la fecha
print(fecha_formateada)
fecha_parseada = datetime.datetime.strptime("17/05/2020","%d/%m/%Y") #convierte string a fecha
print(fecha_parseada)
diferencia = fecha_actual - fecha_especifica #diferencia entre fechas
print(diferencia) #diferencia en dias
print(diferencia.days) #diferencia en dias
print(diferencia.seconds) #diferencia en segundos
nueva_fecha = fecha_actual + datetime.timedelta(days=10) #suma 10 dias a la fecha actual
print(nueva_fecha)

#Libreria OS trabaja con el sistema operativo
import os
print(os.name) #nombre del sistema operativo
print(os.getcwd()) #directorio actual   
print(os.listdir()) #lista de archivos y carpetas en el directorio actual
os.mkdir("nueva_carpeta") #crea una nueva carpeta   
os.rename("nueva_carpeta","carpeta_renombrada") #renombra la carpeta
os.rmdir("carpeta_renombrada") #elimina la carpeta  
print(os.path.exists("libreriasEstandar.py")) #verifica si el archivo existe
print(os.path.isfile("libreriasEstandar.py")) #verifica si es un archivo
print(os.path.isdir("carpeta_renombrada")) #verifica si es una carpeta
print(os.path.join(os.getcwd(),"libreriasEstandar.py")) #une rutas de archivos