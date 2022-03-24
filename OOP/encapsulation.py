from turtle import speed


class car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving")
    def __updateSoftware(self):
        print("Updating Software")

teslacar = car()
teslacar.drive()



class Cars:
    __maxSpeed = 0
    __name = ""

    def __init__(self):
        self.__maxSpeed = 200
        self.__name = "Tesla Car"
    def drive(self):
        print("driving. maxSpeed " + str(self.__maxSpeed))

teslaCar = Cars()
teslaCar.drive()
teslaCar.__maxSpeed = 50
teslaCar.drive

# using the setter methodto change the value of a private variable
def setMaxSpeed(self, speed):
    self.__maxspeed = speed

teslaCar = Cars()
teslaCar.drive()
teslaCar.__setMaxSpeed = 500
teslaCar.drive
