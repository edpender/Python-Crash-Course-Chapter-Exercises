pizzas = ['chicken','peperoni','cheese']
other_pizzas = pizzas[:] 
other_pizzas.append('pineapple')
print("My favourite pizzas are:")
list(map(print,pizzas))
print("My friends favourite pizzas are:")
list(map(print,other_pizzas))
