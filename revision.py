# Revision of some previous learning
cars = ['Bugatti','Verna','BMW-M4']
for car in cars:
    print(car.title()+"these are my favourite cars.")
    print("sound of these cars are like a beast."+car.title())

print("\t list of my favourite cars.")

# Finding prime numbers
for prime in range(0,100,2):
    print(prime)

# Finding square using range and lists
for square in range(1,10):
    print(square**2)

for cube in range(1,10):
    print(cube**3)

print(list(range(1,100)))

quads = []
for value in range(1,10):
    quad = value**4
    quads.append(quad)

print(quads)

# Tuples
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimension_2 = list(range(1,20))
print(dimension_2)
print(dimension_2[6])
print(sum(dimension_2))

my_foods = ['meat','paneer','soybean','curd']
my_favourite_foods = my_foods[:]
print("I love to eating these foods: ")
print(my_foods)
print("I love these foods: ")
print(my_favourite_foods)
my_favourite_foods.append('milk')
print(my_favourite_foods)
print("I remove meat from list.")
my_favourite_foods.remove('meat')
print(my_favourite_foods)

coder = (100,200,300,400,500)
print("\n\tOriginal Tuple:")
for coder in coder:
    print(coder)

coder = (100,200,300,400,500,600)
print("\n\tModified Tuple:")
for coder in coder:
    print(coder)

crushes = ['verna','I-20','Lamborghini']
for crush in crushes:
    if crush == 'Lamborghini':
        print("My Love: "+crush.upper())
    else:
        print(crush.title())

# some more revision
print("Print value of crushes in upper case:")
for crush in crushes:
    print(crush.upper())

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies.")

age = 20
if age != 21:
    print("Wrong answer.")
if age == 20:
    print("Right")
else:
    print("wrong")

