
class Car:
    #DATA
    #Fun
    def __str__(self):
        return f'color {self.color} maxspeed = {self.maxSpeed}'

    def drive(self):
        print('the car is moving')
        self.__brake(self)

    def __brake(self):
        print('stoping . . . ')

    def __init__(self,color,maxSpeed=150):
        print('creating a car .... ')
        self.color=color
        self.maxSpeed=maxSpeed


seat=Car('red',194)
bmw=Car('black',340)
print(seat)
print(bmw)
bmw.__brake()
x=4












