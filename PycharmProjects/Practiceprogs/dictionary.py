'''
people=[{'fname':'ali','lname':'bilal','age':30,'city':'karachi'},
{'fname':'zahid','lname':'ali','age':35,'city':'LHR'},
{'fname':'imran','lname':'adeel','age':32,'city':'karachi'},]

for a in people:
    print("\n"+a.get('fname'),a.get('lname'),a.get('age'),a.get('city'))

'''
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for a in pets:
      print("\n this is what i know about "+pet['name'])
      for key,value in a.items():
            print("\t",key+":",value)


#print(pets)