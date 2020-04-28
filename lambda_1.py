multiply = lambda x,y: x+y
x = int(input("Enter first num:"))
y = int(input("Enter 2nd num:"))
m = multiply(x,y)
print(m)

full_name = lambda f_name,l_name: f_name.title()+" "+l_name.title()
name = full_name('mukul','phougat')
print(name)
