"""
Escribir un programa que guarde en un diccionario los
precios de las frutas de la tabla, pregunte al usuario
por una fruta, un número de kilos y muestre por pantalla
el precio de ese número de kilos de fruta. Si la fruta no
está en el diccionario debe mostrar un mensaje informando
de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
fruitCatalog = {"Plátano": 1.35, "Manzana": 0.8, "Pera": 0.85, "Naranja": 0.7}
print("CATÁLOGO DE FRUTAS")
print("Fruta\t\tPrecio")
for (fruit, price) in fruitCatalog.items():
    print("{}\t\t$ {}".format(fruit, price))
userFruit = input("\nSelecciona una fruta: ")
if userFruit in fruitCatalog:
    userQuantity = float(input("Cantidad en kg: "))
    print("{} kg. de {} = $ {}".format(userQuantity, userFruit, userQuantity * fruitCatalog[userFruit]))
else:
    print("Fruta inexistente")
