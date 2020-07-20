myDictionary = {"Alemania": "Berlin", "Francia": "París", "Chile": "Santiago", "Estados Unidos": "Nueva York"}
print(myDictionary["Alemania"])

myDictionary["Italia"] = "Lisboa"
print(myDictionary)

myDictionary["Italia"] = "Roma"
print(myDictionary)

del myDictionary["Estados Unidos"]
print(myDictionary)

myDictionary["Number"] = 3
myDictionary[3] = "Number"
print(myDictionary)

print(myDictionary.keys())
print(myDictionary.values())
print(len(myDictionary))
