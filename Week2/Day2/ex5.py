from ex4 import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} can use their power: {member['power']}")
                else:
                    raise ValueError(f"{member['name']} is not over 18 years old")

    def incredible_presentation(self):
        print("* Here is our powerful family *")
        super().family_presentation()

# Creating an instance of the Incredibles class
incredibles_family = TheIncredibles(last_name="Incredibles", members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
])

# Calling the incredible_presentation method
incredibles_family.incredible_presentation()

# Using the born method to add Baby Jack with an unknown power
incredibles_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

# Calling the incredible_presentation method again
incredibles_family.incredible_presentation()
incredibles_family.use_power('Michael')
incredibles_family.use_power('Jack')
