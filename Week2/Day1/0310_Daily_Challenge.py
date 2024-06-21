#Create class - Farm, it has only one attribute - name
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

#Create methode - add_animals with 2 parameters - animals and quantity
    def add_animal(self, animal, quantity=1):
        if animal in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity

#Create methode - get_info
    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        return info + "\n  E-I-E-I-O"

    def get_animals_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animals_types()
        animal_count = len(animal_types)
        if animal_count == 1:
            animal_str = animal_types[0]
            if self.animals[animal_str] > 1:
                animal_str += "s"
            return f"{self.name}'s farm has {animals_str}."
        else:
            return f"{self.name}'s farm has no animals."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#    E-I-E-I-0!