# Printing Even numbers using while loop
x = 0
while x <= 10:
    x += 2
    print(x)

# Using continue statement
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# Some more while loop
print("LOOPS:")
y = 1
while y <= 100:
    print(y)
    y += 1

prompt = "\nChoose Pizza toppings:"
prompt += "\nYour choosen pizza toppings are:"
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("\nI'd like to eat that " + topping.title() + " pizza !")
# Exercise tickets
prompt = "\nInox cinemas."
prompt += "\nEnter your age: "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif age == 'exit':
        break
    elif int(age) <= 3:
        print("Free of Cost for childs!!")
    elif int(age) <= 12:
        print("Ticket cost is $10 ")
    else:
        print("Ticket cost is $15")

# While loops using list and Dictionaries
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying Please wait for response " + current_user.title())
    confirmed_users.append(current_user)
    print("The following has been confirmed for the website.")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
