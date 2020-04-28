x = 1
while x <= 5:
    print(x)
    x = x+1
user_info = {}
while True:
    print("enter 'q' any time to quit.")
    f_name = input("Enter your first name:")
    user_info['first name'] = f_name
    if f_name == 'q':
	    break
    l_name = input("Enter your last name:")
    user_info['last name'] = l_name
    if l_name == 'q':
	    break
    print("User details are:"), print(user_info)
