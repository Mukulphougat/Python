# Functions
def greet_user():
    """Display a simple greeting."""
    print("Happy Birday!")
print(greet_user())
def display_message():
    print("\nWhat are you learning in this chapter.")

print(display_message())

def favourite_book(book):
    print("One of my favourite book is " + book.title() + ".")
print(favourite_book('Harry Potter'))

username = input("\nEnter your name. I will give you something better:-")
def greet_user(username):
    print("Hi! " + username.title())

print(greet_user(username.title()))