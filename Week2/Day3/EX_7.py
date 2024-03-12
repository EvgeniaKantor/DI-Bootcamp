from faker import Faker

faker = Faker()
users = []

def add_user():
    user = {
        'name': faker.first_name(),
        'address': faker.street_address(),
        'language_code': faker.language_code()
    }
    users.append(user)

for _ in range(5):
    add_user()

print(users)