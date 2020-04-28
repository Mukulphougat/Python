def make_pizza(size, *toppings):
    print("\nMaking a pizza " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)


def greet_person(f_name, l_name):
    print(f_name.title() + " " + l_name.title() + " OMG! you studied at hogwarts.")
