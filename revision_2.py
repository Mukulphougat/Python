# Some more if statements
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("Is car == 'audi'? I predict false")
print(car == 'audi')

# Simple if statements
age = 20
if age >= 18:
    print("you are old enough to vote.")
# Input
age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet!")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# the if-elif-else chain statement

age = 12
if age < 4:
    print("Fees is 0$")
elif age < 18:
    print("Fees is $5")
else:
    print("you admission cost is 10$")

# some more elif
age = 12
if age <= 14:
    price = 0
elif age <= 18:
    price = 5
elif age <= 65:
    price = 10
else:
    price = 5
print("Your ticket price is--"+str(price))

# Dictionaries
alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

alien_0['david'] = 24
alien_0['carolina'] = 30
print(alien_0)
alien_0['ankit'] = 23
print(alien_0)

# Starting with an empty dictionary
alien_1 = {}

alien_2 = {'color':'age'}
alien_2
