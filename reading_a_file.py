with open('we.txt') as file_object:
    contents = file_object.read()
    print(contents.lstrip())

file_name = 'typing_practice.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)
