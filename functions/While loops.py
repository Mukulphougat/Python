# While loops
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# Letting the using when to quit
prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end program."
message = " "
while message != quit:
    message = input(prompt)

if message != 'quit':
    print(message)