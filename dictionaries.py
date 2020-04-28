# Dictionary in a dictionary
users = {'mphougat': {'first': 'Mukul','last': 'Phougat','Location': 'Bhalout'}, 'hpotter': {'first': 'Harry', 'last': 'Potter','Location': 'Hogwarts'}}
for username, user_info in users.items():
    print("\nUser-name: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['Location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())