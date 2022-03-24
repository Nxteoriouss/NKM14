class Hen(object):
    def feed(self):
        print("eats seeds")

class Duck(object):
    def feed(self):
        print("filter feeding")
def canFeed(birdType):
    birdType.feed()

henObj = Hen()
duckObj = Duck()

canFeed(henObj)
canFeed(duckObj)

#Second Example
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstarct method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstarct method")

class Suv(Vehicle):
    def drive(self):
        return 'Suv is a very comfortable vehicle'

    def stop(self):
        return 'The Suv is easy to control and make it stop'

class Bus(Vehicle):
    def drive(self):
        return 'A bus is a very long vehicle '

    def stop(self):
        return 'Be careful when stopping the bus'

vehiclesObj = [Bus("Goes to CBD"),
Bus("Goes to other places from CBD"),
Suv("Tesla")]

for vehicle in vehiclesObj:
    print(vehicle.name + ':' + vehicle.drive())

class Learner:
    def __init__(self, name):
        self.name = name

    def read(self):
        raise NotImplementedError("Subclass must implement abstarct method")

    def write(self):
        raise NotImplementedError("Subclass must implement abstarct method")

class Pupil(Learner):
    def read(self):
        return 'Pupil can read simple books'

    def write(self):
        return 'The Pupil can write 2 pages of composition'

class Student(Learner):
    def read(self):
        return 'A student can high-level books '

    def write(self):
        return 'A Student can write 4 pages of composition'

learnerSub = [Pupil("Learns in primary school"),
Pupil("learns in international and national schools"),
Student("HighSchool")]

for learners in learnerSub:
    print(learners.name + ':' + learners.read())
