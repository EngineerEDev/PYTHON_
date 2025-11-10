"""🚀 Mini reto final (Día 4)
Combina lo que aprendiste hoy:
Crea una lista de diccionarios, donde cada diccionario represente una persona con claves: "nombre", "edad" y "ciudad".
Agrega al menos 3 personas Recorre la lista con un for y muestra cada persona en formato:"""


lista_personas=[
    {"nombre":"dana","edad":28,"ciudad":"Madrid"},
    {"nombre":"juana","edad":26,"ciudad":"bucaramanga"},
    {"nombre":"lina","edad":30,"ciudad":"Cali"},
    {"nombre":"maria","edad":22,"ciudad":"Barranquilla"}
]

for persona in lista_personas:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}") 