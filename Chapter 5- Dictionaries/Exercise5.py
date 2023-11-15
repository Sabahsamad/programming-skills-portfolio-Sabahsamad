pets = []


pet = {
    'animal type': 'python',
    'name': 'Ball python',
    'owner': 'afnan',
    'weight': 20,
    'eats': ' rats',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'Australorp',
    'owner': 'Sheehan',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'bill',
    'owner': 'alan',
    'weight': 3,
    'eats': 'mice',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")