#Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects using the code provided above
cat1 = Cat('Tom', 11)
cat2 = Cat('Mur', 2)
cat3 = Cat("Flash", 14)

# The function finds the oldest cat and returns the cat
def find_oldest(cat1, cat2, cat3):
    oldest_cat = max(cat1, cat2, cat3, key=lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest(cat1, cat2, cat3)
print(f'The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.')

#Exercise2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

#Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(f'{self.name} goes woof!')

#Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        jump_height = self.height * 2
        print(f'{self.name} jumps {jump_height} cm high!')

#Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
davids_dog = Dog('Rex', 50)
davids_dog.bark()
davids_dog.jump()

#Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog('Teacup', 20)
sarahs_dog.bark()
sarahs_dog.jump()

#Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog
def compare_height(davids_dog, sarahs_dog):
    biggest_dog = max(davids_dog, sarahs_dog, key=lambda dog: dog.height)
    return biggest_dog

biggest_dog = compare_height(davids_dog, sarahs_dog)
print(f"The biggest dog is {biggest_dog.name} with height {biggest_dog.height} cm")

# OR v2 Check which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print("Both dogs are of the same size.")

#Exercise3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

#Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)
#Create an object
stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# Call the sing_me_a_song method
stairway.sing_me_a_song()

#Exercise4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

#3_Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the {self.name}.")
        else:
            print(f"{new_animal} is already added to the {self.name}.")

#4_Create a method called get_animals that prints all the animals of the zoo
    def get_animals(self):
        for animal in self.animals:
                print(animal)

#5_Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list
    def sell_animal(self, animals_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}.")
        else:
            print(f"{animal_sold} is not present in {self.name}.")

#6_Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        return sorted_animals

#7 Create a method called get_groups that prints the animal/animals inside each group
    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            print(f"{key}: {', '.join(value)}")

# Create a Zoo object called ramat_gan_safari
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Zookeeper adds animals to the zoo
print("Which animal should we add to the zoo? --> Giraffe")
ramat_gan_safari.add_animal("Giraffe")
print("Which animal should we add to the zoo? --> Lion")
ramat_gan_safari.add_animal("Lion")
print("Which animal should we add to the zoo? --> Tiger")
ramat_gan_safari.add_animal("Tiger")
print("Which animal should we add to the zoo? --> Elephant")
ramat_gan_safari.add_animal("Elephant")

# Zookeeper checks all the animals in the zoo
ramat_gan_safari.get_animals()

# Zookeeper sells an animal from the zoo
print("Which animal should we sell from the zoo? --> Lion")
ramat_gan_safari.sell_animal("Lion")

# Zookeeper checks all the animals in the zoo after selling
ramat_gan_safari.get_animals()

# Zookeeper sorts and groups the animals
print("Groups of animals in the zoo:")
ramat_gan_safari.get_groups()






