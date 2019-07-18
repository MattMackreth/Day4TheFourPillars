# Four Pillars of Object Oriented Programming
# Abstraction
# Giving the user only the information needed to perform a task
# While keeping unnecessary information away
# Using python modules as an example


class Animal:
    def __init__(self, age, weight, species):
        self.age = age  # Same as age = 15 in non-oop
        self.weight = weight
        self.species = species

    def can_hunt(self, value):
        return value

    def eat(self):
        return 'yum yum yum'

    def sleep(self):
        return 'zzzzzzzzzzzzz'


class Mammal(Animal):
    def __init__(self, age, weight, species, name):
        super().__init__(age, weight, species)
        self.name = name

    def can_speak_a_language(self, can_speak):
        return can_speak


class Bird(Animal):
    def __init__(self, age, weight, species, name, feather_colour):
        super().__init__(age, weight, species)
        self.name = name
        self.feather_colour = self.feather_colour

    def can_fly(self, can_fly):
        return can_fly


class Reptile(Animal):
    def __init__(self, age, weight, species, name, region_found):
        super().__init__(age,weight,species)
        self.name = name
        self.region_found = region_found

    def is_venomous(self, value):
        return value
