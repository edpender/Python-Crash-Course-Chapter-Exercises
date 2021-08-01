person_one = {
        'first_name' : 'Marcus',
        'last_name' : 'Rashford', 
        'age':'23',
        'city' : 'Manchester'}

person_two = {
        'first_name' : 'Lionel',
        'last_name' : 'Messi', 
        'age':'34',
        'city' : 'Barcelona'}

person_three = {
        'first_name' : 'Robert',
        'last_name' : 'Lewandowski', 
        'age':'32',
        'city' : 'Munich'}

persons = [person_one,person_two,person_three]

for person in persons:
    print('Their name is ' + person['first_name'] +' ' +  person['last_name'])
    print("They're " + person['age'] +" years old and live in " + person['city'])
