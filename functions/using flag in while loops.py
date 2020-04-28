# Using flag
prompt = "\nTell me your name, and I will reprint your name: "
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
if message == 'quit':
    active = False
else:
    print(message)