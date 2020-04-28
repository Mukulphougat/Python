# Not using a middle name
def get_formatted_name(first_name, last_name,  middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
magician = get_formatted_name('harry','potter')
print(magician)

# Returning a Dictionary
def build_person(first_name, last_name):
    person = {'first name':first_name, 'last name':last_name}
    return person
magician = build_person('harry', 'potter')
print(magician)
magicians = {'harry-potter age': 20}
print(magicians)