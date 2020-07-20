def basic_operations(a, b):
    return a + b, a - b, a * b, a / b, a ** b, a // b, a % b


A, B = 7, 3

# These two assignations are equivalent
addition, difference, multiplication, division, exponent, integerPart, module = basic_operations(A, B)
results = basic_operations(A, B)

print("A =", A, "\tB =", B, "\n")

print("Addition: \t\t\t", addition)
print("Difference: \t\t", difference)
print("Multiplication: \t", multiplication)
print("Division: \t\t\t", division)
print("Exponent: \t\t\t", exponent)
print("Integer part: \t\t", integerPart)
print("Module: \t\t\t", module)

for i, result in enumerate(results):
    print(i + 1, ":", result)
