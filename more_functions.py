#More functions
def build_profile(first_name, last_name):
    print(first_name.title()+" "+last_name.title()+" Nice name.")
        
build_profile('harry', 'potter')

# More
def user_name(first, last):
    full = first+" "+last
    return full.title()


wizard = user_name('harry', 'potter')
print(wizard)



def build_wizard(first_name, middle_name, last_name):
    full_name = first_name+" "+middle_name+" "+last_name
    return full_name.title()
while True:
    print("Please tell me your name.")
    print("Enter 'q' any time to quit")
    first_name = input("Enter first name.")
    if first_name == 'q':
        break
    middle_name = input("Enter your middle name.")
    if middle_name == 'q':
        break
    last_name = input("Enter last name.")
    if last_name == 'q':
        break
    full_name = build_wizard(first_name, middle_name, last_name)
    print(full_name+" OMG! you defeat the voldemort... i m big fan of you")




        
