class friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myself(self):
        print('Hey! my name is ' + self.name + '.')

    def myage(self):
        print("I'm " + str(self.age) + " year's old.")

me = friend("Mukul", 21)
print(me.name)
print(me.age)
me.myself()
me.myage()
me.age = 20
print(me.age)
del me.age 
