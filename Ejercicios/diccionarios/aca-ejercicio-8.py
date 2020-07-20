"""
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos
puntos, y cada par <palabra>:<traducción> separados por comas. El programa
debe crear un diccionario con las palabras y sus traducciones. Después
pedirá una frase en español y utilizará el diccionario para traducirla
palabra a palabra. Si una palabra no está en el diccionario debe dejarla
sin traducir.
"""
translate = {}
codifiedTranslate = input(
    "Introduce las traducciones en formato <palabra 1>:<traducción 1>,<palabra 2>:<traducción 2>,(...) ")
codifiedTranslate = codifiedTranslate.split(",")
for pair in codifiedTranslate:
    translation = pair.split(":")
    translate.update({translation[0]: translation[1]})
sentence = input("Ingresa una frase para traducir: ")
sentence = sentence.split(" ")
i = 0
for word in sentence:
    if word in translate:
        sentence[i] = translate[word]
    i += 1
print(" ".join(sentence))