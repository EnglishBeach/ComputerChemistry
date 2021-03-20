# class Random_range(object):
#     def __init__


class Vehicle(object):
    def __init__(self, size, color='Black', material='Steel'):
        self.color = color
        self.material = material
        self.size = size

    def broke(self):
        return 'Broken %s car maden from %s' % (self.size, self.material)

    def drive(self):
        return 'Driving %s %s car right now!' % (self.size, self.color)


inpsize = input("Input Vehicles's size: ")
car1 = Vehicle(size=inpsize, color='Red', material='Wood')
print(type(car1))
