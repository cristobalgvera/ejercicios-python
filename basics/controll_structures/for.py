for i in [1, 2, 3]:  # 'for' loop hasn't a count variable itself
    print(i, "veces")

print()
for name in ["Cristóbal", "Daniela", "Víctor", "Jorge", "Ricardo"]:
    print(name)

# By default print add a '\n' at the end of each instruction, to delete it do that
for char in "cristobalgajardo.v@gmail.com":
    print(char, end=" ")  # You can add whatever you want

# Validate an email (simple way)
isEmail = False

email = input("\n\nEmail: ")

for char in email:
    if char == "@":
        isEmail = True

if isEmail:
    print("Valid email")
else:
    print("Invalid email")

for i in range(2, 15, 3):  # Range from 2 to 14 (5 - 1) with step 3
    print("Variable value: {}".format(i))
    print(f"Variable value: {i}")  # This annotation is called f function and do same as above print()

email = "cristobalgajardo.v@gmail.com"
for i in range(len(email)):
    print(i)  # Write numbers from zero to n, where n is length of string 'email'

# Continue statement
for char in email:
    if char == "@":
        print("|", end="")
        continue
    print(char, end="")

print("\n")
i = 0
for char in input("Your full name: "):
    if char == " ":
        continue
    i += 1

print("Your name has {} characters without count spaces".format(i))
