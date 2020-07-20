myList = ["Cristóbal", "Daniela", "Víctor", "Jorge", "Ricardo"]
print(myList)

myList.append("María")
print(myList)

myList.insert(3, "Eduardo")
print(myList)

myList.extend(["Sandra", "Ana", "Cristian"])
print(myList)

print(myList[2])
print(myList.index("Cristóbal"))
print("Mario" in myList)

myList.remove("Cristian")
print(myList)

myList.pop(-3)
print(myList)

myList_2 = ["Esteban", 5]

myList_3 = myList + myList_2

print(myList_3)
