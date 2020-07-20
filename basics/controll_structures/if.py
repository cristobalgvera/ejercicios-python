def evaluation(a):
    if 0 <= a < 2:  # Is possible concatenate many comparators -> e.g: a < b < c < d and e > f
        result = "Rejected"
    elif 2 <= a < 5:  # Same to else if instruction
        result = "Try again"
    elif a > 10:
        result = "Invalid qualification"
    else:
        result = "Approved"
    return result


qualification = float(input("Type your qualification: "))
print(evaluation(qualification))

possible_qualifications = list(range(11))  # List from 0 to 10

# To this case is not relevant, but 'in' is case sensitive (Python is case sensitive)
if qualification in possible_qualifications:
    print("Qualification is a possible one")
else:
    print("Qualification isn't a possible one")
