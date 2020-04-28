# Making a profile of a friend
def friend_profile(f_name, l_name, **user_info):
    profile = {}
    profile['First Name'] = f_name
    profile['Last Name'] = l_name 
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(friend_profile('eleven', 'hopper', fav_food = 'wafer', birth = 'hawkins', first_love = 'mike'))

