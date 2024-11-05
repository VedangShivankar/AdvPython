class Vehicle:
    def general_usage(self):
        print("general use : transportation")

class Car(Vehicle):
    def __init__(self):
        print("im car")
        self.wheels = 4
        self.has_roof = True


    def specific_usage(self):
        self.general_usage()
        print("specific use : driving to work , meeting family")

class Motorcycle(Vehicle):
        def __init__(self):
            print("im motorcycle")
            self.wheels = 2
            self.has_roof = False

        def specific_usage(self):
            self.general_usage()
            print("specific use : road trip , racing")

    

c = Car()
c.general_usage()
c.specific_usage

m = Motorcycle()
m.specific_usage()
m.general_usage()