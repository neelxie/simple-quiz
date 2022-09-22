class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Make: {self.make} \n Model: {self.model} \n Year: {self.year}"

    def start(self):
        print(" The {}, {}, {} is starting.".format(self.make,self.model, self.year ))

    def stop(self):
        print(" The {}, {}, {} is stopping.".format(self.make,self.model, self.year ))

    def drive(self):
        print(" The {}, {}, {} is driving.".format(self.make,self.model, self.year ))

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.color = color
        super().__init__(make, model, year)

    def park(self):
        print(" The {} {}, {}, {} is parking".format(self.make,self.model, self.year, self.color ))

my_car = Car("Range Rover", "Autobiography", "2021", "black")
my_car.start()
my_car.stop()
my_car.drive()
my_car.park()
