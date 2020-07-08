"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>.
"""
user = {"name": input("Nombre: "), "age": int(input("Edad: ")),
        "address": input("Dirección: "), "phone": input("Teléfono: ")}
msg = "{} tiene {} años, vive en {} y su número de teléfono es {}"
print(msg.format(user["name"], user["age"], user["address"], user["phone"]))
