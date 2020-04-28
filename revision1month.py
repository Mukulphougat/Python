# Revision of python after exams.....
My_favourites = []
My_favourites.append('Eleven')
My_favourites.insert(0,'Mike')
My_favourites.append('Steve')
My_favourites.append('Will')
My_favourites.append('Harry')
My_favourites.append('Harmoine')
My_favourites.append('Rupert')
print("I got these persons in my 20 years of life"),print(My_favourites)
print("From stranger's things i like these persons too much: "+My_favourites[0]+", "+My_favourites[1]+".")
print("From Harry Potter series i like these characters: "+My_favourites[4]+", "+My_favourites[5]+".")
# Copying a list to another list
favourite_things = My_favourites
print(favourite_things)
# Removing an item from a list using pop() method
favourite_things.pop(0)
print('I removed Mike from the list'),print(favourite_things)
My_favourites.insert(0, 'Mike') # I insert again Mike in the list
print(favourite_things)

favourite_things.sort()
print(favourite_things)

favourite_things.sort(reverse=True)
print(favourite_things)
for person in favourite_things:
    print("My favourite persons are: "),print(person.title())

print("Number of persons in the list:-"),print(len(favourite_things))


# working with lists
favourite_persons = ['Eleven','Mike']
print(favourite_persons)
for person in favourite_persons:
    print(favourite_persons[0].title()+" "+"I loves Millie Bobby Brown......")
    print(favourite_persons[1].title()+" "+"I like Mike in stranger things Tv serires.")

for value in range(0,100,2):
    print(value)

squares = []
for value in range(0,11):
    square = value**2
    squares.append(square)

print(squares)
