"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario.
"""
persona = {}
print("DEJA AMBOS CAMPOS VACÍOS PARA FINALIZAR\n")
while True:
    key = input("Característica: ")
    map = input("Valor: ")
    if not (key in persona) and key != "":
        persona.update({key: map})
        print("{}\n".format(persona))
    elif key == "" and map == "":
        break
    else:
        print("No puedes añadir una característica ya existente o nula\n")
print("\nDatos del diccionario:\n\n{}".format(persona))
