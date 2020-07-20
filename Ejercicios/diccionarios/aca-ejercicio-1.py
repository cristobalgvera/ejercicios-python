"""
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por
una divisa y muestre su símbolo o un mensaje de aviso si la divisa
no está en el diccionario.
"""
diccionario = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa = input("Nombra un tipo de divisa: ")
if divisa in diccionario:
    print("{}: {}".format(divisa, diccionario[divisa]))
else:
    print("'{}' no es parte del diccionario".format(divisa))