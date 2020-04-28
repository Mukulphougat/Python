# Some more dictionaries
alien_1 = {'name':'david'}
alien_1['name'] = 'marie'
print(alien_1)


# some more
alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position: " + str(alien_0['x_position']))

# Some more
print(alien_0)
del alien_0['speed']
print(alien_0)

# Favourite languages
favourite_languages = {
    'jen':'python',
    'sarah':'c#',
    'edward':'ruby',
    'phil':'python'
}
for name, langauge in favourite_languages.items():
    print("\n" + name.title()+" favourite language is: " + langauge.title())
print("sarah favourite language is: "+favourite_languages['sarah'].title())
print("jen favourite language is: "+favourite_languages['jen'].title())

# Looping through dictionaries
user_0 = {
    'username':'efermi',
    'first':'emrico',
    'last':'fermi'
}
for key, value in user_0.items():
    print("\nkey: " + key)
    print("value: " + value)

# Looping through all the keys in dictionary
favourite_languages_1 = {
    'mukul' : 'python',
    'sahil' : 'animation',
    'jay' : 'c'
}
for value in favourite_languages_1.values():
    print("\n" + value.title())

# display a message about their favourite languages
favourite_languages_2 = {
    'mukul' : 'Python',
    'half-blood-prince' : 'R'
}
friends = ['mukul','half-blood-prince']
for name in favourite_languages_2.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_languages_2[name].title() + "!")

# for taking a poll
favourite_languages_3 = {
    'hbp' : 'python',
    'mukul' : 'R',
    'cobra' : 'c#'
}
if 'mo-farah' not in favourite_languages_3.keys():
    print("mo-farah, please take our poll.")

# sorting in dictionaries
favourite_languages_4 = {
    'snape' : 'Python',
    'harry' : 'R',
    'ron' : 'c#',
    'harmonie' : 'python'
}
for name in sorted(favourite_languages_4.keys()):
    print("\n" + name.title() + ", thank you for taking the poll.")

for language in favourite_languages_4.values():
    print("\n" + language.title())

# some more for stop duplication
languages = {
    'mukul' : 'python',
    'sahil' : 'C#',
    'jay' : 'python'
}
for language in set(languages.values()):
    print(language.title())