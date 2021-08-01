fruits = ['apple','orange','banana','pineapple','kiwi','pomegranate',
'grapes','pears','strawberry','watermelon','lemon','mango']

def is_inside(object,list):
    if object in list:
        print("Yes "+object+ " is in fruits")
    else:
        print("No " + object + " is not in fruits")

is_inside('tomato',fruits)
is_inside('apple',fruits)
