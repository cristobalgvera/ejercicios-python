def addition(a, b):
    return a + b


def difference(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


try:
    A = int(input("First number: "))
    B = int(input("Second number: "))
    action = input("Type one operation to do: ('addition', 'difference', 'multiplication', 'division')\n")
    if action == "addition":
        print(addition(A, B))
    elif action == "difference":
        print(difference(A, B))
    elif action == "multiplication":
        print(multiplication(A, B))
    elif action == "division":
        print(division(A, B))
    else:
        print("Invalid type")
except ZeroDivisionError:
    print("Isn't possible divide by zero")
except ValueError:
    print("Are you typing correct numbers?")
finally:
    print("Operation complete")


# Raise can set a custom message for an existent exception. Exceptions are classes
def evaluate_age(age):
    paragraph = "You're old"
    if age < 0:
        raise TypeError("You can't have a negative age")
    if 0 <= age <= 20:
        paragraph = "You're so young"
    elif 20 < age <= 40:
        paragraph = "You're young"
    elif 40 < age <= 65:
        paragraph = "You're mature"
    return paragraph


try:
    print(evaluate_age(int(input("Insert your age: "))))
except TypeError as error:
    print(error)
finally:
    print("Completed execution")
