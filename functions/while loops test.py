# while loops
sandwich_orders = ['chicken sandwich', 'cheese sandwich', 'potato sandwich', 'cheese sandwich', 'cheese sandwich', 'pork sandwich']
print(sandwich_orders)
while 'cheese sandwich' in sandwich_orders:
    sandwich_orders.remove('cheese sandwich')
print(sandwich_orders)
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(sandwich.title() + " wait your order is in processing.... ")
    finished_sandwiches.append(sandwich)

print("Get your sandwiches")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title() + " That's nice choice!")

