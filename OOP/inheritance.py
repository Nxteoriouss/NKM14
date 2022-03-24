class Person:
    def __init__(self):
        print("Person class is ready")
    def whoisThis(self):
        print("Person")

    def walk(self):
        print("Walk to any direction")

class Adult(Person):

    def __init__(self):
        super().__init__()
        print("Adult is ready")

    def whoisThis(self):
        print("Adult")

    def read(self):
        print("Reading")

chirles = Adult()
chirles.whoisThis
chirles.walk()
chirles.read()

class Vehicle:
    def __init__(self):
        print("Vehicle class is ready")
    def whoisThis(self):
        print("Vehicle")

    def drive(self):
        print("drive to anywhere")

class Heavy(Vehicle):

    def __init__(self):
        super().__init__()
        print("Heavy is ready")

    def whoisThis(self):
        print("Heavy")

    def carry(self):
        print("Carry heavy goods")

chirles = Heavy()
chirles.whoisThis
chirles.drive()
chirles.carry()