pet_one = {
        'name': 'bonnie',
        'species':'dog',
        'owner': 'yvonne'
        }

pet_two = {
        'name': 'ghost',
        'species':'horse',
        'owner': 'leah'
        }

pet_three = {
        'name': 'tilly',
        'species':'cat',
        'owner': 'eoghan'
        }

pets = [pet_one,pet_two,pet_three]

for pet in pets:
    print("Their name is " + pet['name'].title() + '.')
    print("It's a " + pet['species'].title() + '.')
    print("The owner is " + pet['owner'].title() + '.')
