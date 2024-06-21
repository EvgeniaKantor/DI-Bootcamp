# exercise 3
import random as rd
from d0311_Exercise_XP import Dog

class PetDog(Dog):
    #class variable
    sentences = {1:"does a barrel roll", 2:"stands on his back legs", 3:"shakes your hand",
                 4:"plays dead"}
    names =[]
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
        PetDog.names.append(name)
    def train(self):
        self.bark()
        self.trained = True
    def play(self, *names):
        print(", ".join(names)+' all play together')
    def do_a_trick(self):
        if self.trained:
            com_num = rd.randint(1,4)
            full_sentence = self.name +" " + PetDog.sentences[com_num]
            print(full_sentence)
        else:
            print("Sorry dog is not trained")

dog1 = PetDog("Nice", 20, 3)
dog2 = PetDog("Pretty", 10,11)
dog3 = PetDog("Simpson", 3, 9)

dog1.train()
dog3.train()
dog1.play(*PetDog.names)
dog1.do_a_trick()
dog2.do_a_trick()
dog3.do_a_trick()



