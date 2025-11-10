freses=[
    "La vida es como una caja de chocolates, nunca sabes lo que te va a tocar.",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.",
    "No cuentes los días, haz que los días cuenten.",
    "python es un lenguaje de programación"
    ]

for frase in freses:
    print(frase)
    listafrase=frase.split()
    print("cantidad de palabras", len(listafrase))
    print("Frase en mayúsculas:", frase.upper())
    print(f"la frase contiene la palabra python: {'python' in frase}")
      
    
    
