# Passing Arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a "+ animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

print(describe_pet('cat', 'little'))
print(describe_pet('dog', 'tom'))
print(describe_pet('tom', 'dog')) # This gives wrong results
print(describe_pet(pet_name='tom', animal_type='dog')) # Keyword arguments

# Setting default values for parameters
def best_friend(friend_name, friend_type='best'):
    print("\nMy " + friend_type + " friend are:")
    print("My " + friend_type + "'s friend is " + friend_name.title())

print(best_friend(friend_name='harry'))
print(best_friend('harmoine'))
print(best_friend('ronald'))
print(best_friend(friend_type='worst', friend_name='preet'))

# Test
def make_shirt(shirt_size, shirt_type='T-shirt'):
    print("\nI want to buy a " + shirt_type.title() + ".")
    print("\nMy size is " + shirt_size.title() + "!")

print(make_shirt('XL'))

# City is in whcih country
def describe_city(city_name, country_name='norway'):
    print("\nI want to settle in " + city_name.title() + " that is in " + country_name.title() + "!")

print(describe_city('oslo'))
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

magician = get_formatted_name('harry', 'potter')
print(magician)

def my_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

loser = my_name('mukul', 'phougat')
print(loser)
# Making an argument optional
def name(first_name, middle_name, last_name):
    full_name = first_name +' '+middle_name+' '+last_name
    return full_name.title()
magician = name('harry','james', 'potter')
print(magician)

def build_person(first_name, last_name, age=' '):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return(person)
musician = build_person('harry', 'potter', age=21)
print(musician)

# Using a function with while loop
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
while True:
    print("\nPlease enter your full name.")
    f_name = input("First name: ")
    if f_name =='quit':
        break
    l_name = input("last name: ")
    if l_name =='quit':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHelllo, "+ formatted_name+ "!")