"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
y muestre por pantalla la misma fecha en formato dd de <mes> de
aaaa donde <mes> es el nombre del mes.
"""
months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre",
          "Octubre", "Noviembre", "Diciembre")
userDate = input("Ingrese fecha en formato DD/MM/YYYY: ")
date = userDate.split("/")
print("{} de {} de {}".format(date[0], months[int(date[1]) - 1], date[2]))
