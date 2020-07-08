"""
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la
lista de la compra y el coste total, con el siguiente formato

Lista de la compra
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""
shoppingList, i, total = {}, 0, 0
print("DEJA ARTÍCULO VACÍO PARA FINALIZAR\n")
while True:
    i += 1
    article = input(f'Artículo N°{i}: ')
    if not (article in shoppingList) and article != "":
        price = float(input("Valor: $ "))
        shoppingList.update({article: price})
        print()
    elif article == "":
        break
    else:
        print("No puedes añadir un artículo ya existente o nulo\n")
print("\nLISTA DE COMPRA\n")
i = 0
for article, price in shoppingList.items():
    i += 1
    print(f"{i}.\t{article.ljust(10)}\t$ {price}")
    total += price
print(f"\t{'TOTAL'.ljust(10)}\t$ {total}")