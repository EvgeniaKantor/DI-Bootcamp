class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family! New member born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(
                f"Name: {member['name']}, Age: {member['age']}, "
                f"Gender: {member['gender']}, Child: {member['is_child']}")

# Creating an instance of the Family class
my_family = Family(last_name="Smith", members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
])

# Calling the methods
my_family.born(name='John', age=0, gender='Male', is_child=True)
print("Is Michael over 18?", my_family.is_18('Michael'))
my_family.family_presentation()

# born and one more presentation
my_family.born(name='Emily', age=0, gender='Female', is_child=True)
my_family.family_presentation()