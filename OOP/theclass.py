class Person:
    "This is a person Class shown here"
    age = 14

    def greet(self):
        print("Hello World")

DavidObj = Person()

print(Person.age)
print(Person.greet)
print(Person.__doc__)
DavidObj.greet() # Person.greet(DavidObj)
