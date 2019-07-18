from FourPillars.Abstraction import Reptile

class Snake(Reptile):
    def __init__(self, age, weight, species, name, region_found, fangs_num, length):
        super().__init__(age, weight, species, name, region_found)
        self.fangs_num = fangs_num
        self.length = length

    def can_constrict(self, bool_value):
        return bool_value

    def can_swim(self, bool_value):
        return bool_value

python = Snake(35, 450, 'Pythoras Scarius', 'Borris', 'Moorgate', 0, 12)
print(python.length, python.fangs_num, python.age, python.name, python.species, python.region_found, python.weight)
print(python.can_constrict(True))
print(python.can_swim(True))
