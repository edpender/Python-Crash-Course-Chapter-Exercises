my_foods = ['pizza', 'chicken', 'fish']
friend_foods = my_foods[:]
friend_foods.append('beef')
print("My favorite foods are:")
list(map(print,my_foods))
print("\nMy friend's favorite foods are:")
list(map(print,friend_foods))
