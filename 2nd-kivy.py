

def dream_city(city, country):
    location = city+", "+country
    return location.title()

while True:
    print("\nEnter the city:")
    print("(Enter 'q' any time quit)")

    city = input("City: ")
    if city == 'q':
        break
    country = input("Country: ")
    if country == 'q':
        break
    abroad = dream_city(city, country)
    print("\nI want to settle in "+ abroad +"!")
