class User:
    pass

user1 = User()
user1.first_name = "Mike"
user1.last_name = "Wheeler"
print(user1.first_name)

user2 = User()
user2.first_name = "Eleven"
user2.last_name = "Hooper"
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)
user1.age = 16
user2.age = 16
user2.favourite_food = 'Wafer'
print(user1.age)
print(user2.age)
print(user2.favourite_food)

