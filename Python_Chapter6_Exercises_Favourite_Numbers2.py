favorite_numbers = {
    'ed': [7, 10],
    'phil': [23, 17, 50],
    'john': [7, 12],
    'ruth': [1000000, 10, 25],
    'russell': [0, 3, 15],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
