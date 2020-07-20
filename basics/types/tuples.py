myTuple = ("Cristóbal", "Daniela", "Víctor", "Jorge", "Ricardo", "Ricardo")
print(myTuple)

myList = list(myTuple)
myList.append("Rodrigo")
print(myList)

myTuple = tuple(myList)
print(myTuple)

print("Cristóbal" in myTuple)

print(myTuple.count("Ricardo"))

print(len(myTuple))

# Tuple unpack
first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh = myTuple

print(second_name)

# Unit tuple
myTuple_2 = ("Esteban",)
print(len(myTuple_2), type(myTuple_2))

# Not recommended way to set tuples
myTuple_3 = "Ricardo", 3, 7, 8, True
print(len(myTuple_3), type(myTuple_3))
