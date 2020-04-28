# checking age using int() function
age = input("How old are you? ")
age = int(age)
print(age >= 18)
if age >= 18:
    print("you are able to vote.."+" "+"You registered for voting.."+" "+"also for driving license!")
else:
    print("your age is not enough for voting! ")

# more inputs
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou are tall enough to ride.. ")
else:
    print("\nYou'll be able to ride when you're a little older.. ")

