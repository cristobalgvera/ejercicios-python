i = 1
while i <= 10:
    print(i)
    i += 1

while True:
    number = int(input("Your number: "))
    if number > 0:
        break
    else:
        print("Number must be greater than 0")

print("Done!")
