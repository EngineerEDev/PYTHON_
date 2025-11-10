with open("notas.txt", "w") as notas:
    notas.write("cada dia es una oportunidad para ser una mejor persona.\n")
    notas.write("la vida es de alto y bajos, disfruta cuando estes arriba, aprende cuando a bajo estes.\n")
    notas.write("nunca dejes de aprender, la vida nunca deja de enseñar.\n")


with open("notas.txt", "r") as notas:
    contenido = notas.read()
    print("Contenido de notas.txt:")
    print(contenido)