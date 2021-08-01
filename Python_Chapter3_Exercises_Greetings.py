#This solution takes concepts, which are introduced later in the book and uses them. 
#For a solution for an exercise similiar to this, look at own_list.py

friends = """Ed Pender
Dylan Reilly
Paul Moore
Stephen Lyons
Ger Hunston
Jamie Reilly
Seana Collins
""".split()

for i in range(int(len(friends)/2)):
   print("Hello " + friends[2*i] +" "+ friends[2*i+1]+ "! How are you?")
