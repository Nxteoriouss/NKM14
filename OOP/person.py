class House:
    category = "house"
    def __init__(self, name, color, type, year, location, owner):
        self.name = name
        self.color = color
        self.type = type
        self.year = year
        self.location = location
        self.owner = owner
A = House("A", "Blue", "Mansion", 2012, "Langata", "John")
B = House("B", "Red", "Mansionette", 2016, "Loresho", "Mary")
C = House("C", "Beige", "Bungalow", 2004, "Uthiru", "David")

print("A is a {}".format(A.__class__.category))
print("B is a {}".format(B.__class__.category))
print("C is a {}".format(C.__class__.category))

print("{} is a {} {} built in {} in {} by {}".format(A.name, A.color, A.type, A.year, A.location, A.owner))
print("{} is a {} {} built in {} in {} by {}".format(B.name, B.color, B.type, B.year, B.location, B.owner))
print("{} is a {} {} built in {} in {} by {}".format(C.name, C.color, C.type, C.year, C.location, C.owner))

class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self, marathon):
        return "{} runs a {} marathon".format(self.name, marathon)

    def read(self):
        return "{} is now reading".format(self.name)
john = Persons("John",  15)

print(john.run("42km"))
print(john.read())