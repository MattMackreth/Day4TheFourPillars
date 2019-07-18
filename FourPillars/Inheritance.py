# Four Pillars of Object Oriented Programming
# Inheritance


class Vehicle:  # Super class
    def __init__(self, make, colour, engine_size, year):
        self.make = make
        self.colour = colour
        self.engine_size = engine_size
        self.year = year
        self.speed = 0

    def start(self):
        vroom = 'vroooooooooooom'
        return vroom

    def stop(self):
        return 'Screeeeeeeech'

    def accelerate(self):
        self.speed += 1
        return self.speed


class Truck(Vehicle):  # Subclass
    def __init__(self, make, colour, engine_size, year, trailer_size):
        super().__init__(make, colour, engine_size, year)
        self.trailer_size = trailer_size


class Boat(Vehicle):
    def __init__(self, make, colour, engine_size, year, num_of_sails, name, num_of_cannons):
        super().__init__(make, colour, engine_size, year)
        self.num_of_sails = num_of_sails
        self.name = 'HMS ' + name
        self.sunk = False
        self.num_of_cannons = num_of_cannons

    def sink(self):
        self.sunk = True
        return 'Oh noooo!'

    def firecannons(self):
        if self.num_of_cannons >= 1:
            return 'FIRE!!!'
        else:
            return 'You have no cannons!'
#
# my_truck = Truck('Ford', 'Silver', 7.5, 2019, 18)
# print(f'Omid has a {my_truck.colour} {my_truck.make} of size {my_truck.engine_size} from {my_truck.year} and trailer size {my_truck.trailer_size}')
# for x in range(0, 3):
#     print(my_truck.accelerate())
#
# my_car = Vehicle('Honda', 'Red', 1.6, 1995)
# print(f'Daniel has a {my_car.colour} {my_car.make} of size {my_car.engine_size} from {my_car.year}')

my_boat = Boat('Yamaha', 'blue', 25.6, 2016, 4, 'Unsinkable', 3)
print(f'Matt has a {my_boat.colour} {my_boat.make} boat called {my_boat.name} of size {my_boat.engine_size} from {my_boat.year} with {my_boat.num_of_sails} sails and {my_boat.num_of_cannons} cannons')
print(my_boat.firecannons())
no_cannon_boat = Boat('Rowboat', 'beige', 0, 1832, 0, 'Smallboat', 0)
print(no_cannon_boat.firecannons())
print(my_boat.sunk)
print(my_boat.sink())
print(my_boat.sunk)
