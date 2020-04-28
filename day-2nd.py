# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

# More dictionary
aliens_1 = []
for alien_number in range(1,31):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_1.append(new_alien)
for alien in aliens_1[:5]:
    print(alien)

print("....")

print("Total number of aliens: " + str(len(aliens_1)))

# changing values of first five aliens
aliens_2 = []
for alien_number in range(0,50):
    new_alien = {'color': 'green', 'points': '10', 'speed': 'slow'}
    aliens_2.append(new_alien)

print("total: " + str(len(aliens_2)))
print(aliens_2)
for alien in aliens_2[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens_2[0:5]:
    print(alien)

# A list in Dictionary
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print("You are ordered a " + pizza['crust'] + "with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

# Nest a list inside dictionary
favourite_languages = {
    'mukul': ['Python', 'R'],
    'harry-potter': ['SQL', 'C#'],
    'granger': ['C', 'C++'],
    'ron': ['HTML', 'PHP']
}
for name, languages in favourite_languages.items():
    print("\n" + name.title() + "Your favourite programming languages are following: ")
    for language in languages:
        print("\t" + language.title())

# A dictionary in dictionary
users = {'mphougat': {'first': 'Mukul','last': 'Phougat','Location': 'Bhalout'}, 'hpotter': {'first': 'Harry', 'last': 'Potter','Location': 'Hogwarts'}}
for username, user_info in users.items():
    print("\nUser-name: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['Location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())