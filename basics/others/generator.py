# Similar to a traditional function but use word 'yield' to return object.
# Generators returns one object at time.
# i.e: if you request for a list, generator will return just one object of
# that list.


def generate_even_return(upper_limit=0):
    my_list = [0]
    m = 1
    while my_list[m - 1] <= upper_limit:
        my_list.append(m * 2)
        m += 1
    my_list.pop()
    if len(my_list) != 0:
        my_list.pop(0)
    return my_list


def generate_even_yield(upper_limit=0):
    n = 1
    if upper_limit != 0:
        while n * 2 <= upper_limit:
            yield n * 2  # Yield is a reserved word for generators
            n += 1


generated_numbers = generate_even_return(10)
print(generated_numbers, type(generated_numbers))

generated_numbers = generate_even_yield(10)
for i in generated_numbers:
    print(i, end=" ")
print(type(generated_numbers))

# Generator just works up to extract one value, after that, element itself is in a
# 'stand by' state waiting for another call, and so on.
generated_numbers = generate_even_yield(10)  # Is necessary call another instance of generator.
print("\nFirst call")
print(next(generated_numbers))  # First call, just one action. After that, stand by state.

print("Second call")
print(next(generated_numbers))
# Difference between traditional functions and generator is, in general, in terms of efficiency


def return_cities(*cities):
    for city in cities:
        yield from city  # Yield from help us to return a sub element of the yield element


returned_cities = return_cities("Temuco", "Angol", "Victoria", "Santiago", "Chiloé")
print("\nFirst call")
print(next(returned_cities))

print("Second call")
print(next(returned_cities))

