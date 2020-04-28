from more_function_tricks import build_wizard as bw
bw('harmoine', 'granger')

from more_function_tricks import build_magician as bm
wizard = bm('harry', 'potter', 20)
print(wizard)
while True:
    print("\nEnter 'q' any-time to exit.")
    f_name = input("enter first name:")
    if f_name == 'q':
        break
    l_name = input("enter your last name:")
    if l_name == 'q':
        break
    age = input("enter your age:")
    if age == 'q':
        break
    full_name = bm(f_name, l_name, age)
    print(full_name)
    print(" OMG! you really defeat the voldemort.")