# Runners group
runners = ['harry', 'ron', 'harmoine']
our_group = ['mukul']
while runners:
    athlete = runners.pop()

    print("Adding user: " + athlete.title())
    our_group.append(athlete)
print("That's our group:- ")
for our_group in our_group:
    print(our_group.title() + " from harry potter!")

Dream_vacation = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    location = input("Which is your dream vacation ?")

    Dream_vacation[name] = location
    repeat = input("would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False
print("\n ---- Poll Results ---- ")
for name, location in Dream_vacation.items():
    print(name + " ok you want to go " + location.title() + " !")