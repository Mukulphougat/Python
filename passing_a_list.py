# passing a list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['harry potter','ron weasly','harmoine granger']
greet_users(usernames)

unprinted_designs = ['iphone case', 'robot pendant', 'dodechedron']
completed_designs = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing Model: " + current_design)
    completed_designs.append(current_design)
print("\nThe following models have been printed:")
for completed_design in completed_designs:
    print(completed_design)
# Some more functions
def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing designs: " +  current_design)
        completed_designs.append(current_design)

def show_completed_designs(completed_designs):
    print("\nThe following designs have been printed:")
    for completed_design in completed_designs:
        print(completed_designs)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []
print(unprinted_designs, completed_designs)
show_completed_designs(completed_designs)

print_models(unprinted_designs[:], completed_designs)
