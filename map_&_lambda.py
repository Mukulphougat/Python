# Using lambda and map on integer values.

some_num = list(range(1,11))
formats = map(lambda x: x+x,some_num)
a = list(formats)
print(a)

# Using lambda and map on string values.

name = ['mukul','phougat']
formatted_name = map(lambda x: x.title(),name)
print(list(formatted_name))
