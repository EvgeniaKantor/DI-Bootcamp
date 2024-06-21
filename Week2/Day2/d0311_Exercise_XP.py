#Exercise1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Creating instances of the three cat breeds
bengal_cat = Bengal("Bengal Cat", 5)
chartreux_cat = Chartreux("Chartreux Cat", 3)
siamese_cat = Siamese("Siamese Cat", 4)

# Creating a list containing all the cat instances
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Creating an instance of the Pets class with all_cats as the argument
sara_pets = Pets(all_cats)

# Taking all the cats for a walk
sara_pets.walk()

#Exercise2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f'{self.name} won the fight'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

dog1 = Dog('Max', 2, 50)
dog2 = Dog('Nip', 5, 19)
dog3 = Dog('Jack', 18, 70)

# Testing the methods
print(dog1.bark())
print(f"{dog1.name}'s running speed: {dog1.run_speed()} m/s")

print(dog2.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()} m/s")

print(dog3.bark())
print(f"{dog3.name}'s running speed: {dog3.run_speed()} m/s")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


#Exercise3
#Create a new python file and import your Dog class from the previous exercise.
