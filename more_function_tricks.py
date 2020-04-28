def build_wizard(f_name, l_name):
    full_name = f_name.title() + " " + l_name.title()

    print(full_name),print(" OMG! you studied from hogwarts and are you in the team to kill voldemort.")

def build_magician(f_name, l_name, age=' '):
    full_name = {'first name':f_name.title(), 'last name':l_name.title()}
    if age:
        full_name['age'] = age
    return full_name


