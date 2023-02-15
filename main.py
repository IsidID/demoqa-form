from faker import Faker
fake = Faker()
import random


def generate_user():
    firstName = fake.word()
    lastName = fake.word()
    email = fake.email()
    randomDigit = str(random.randint(1, 3))
    phone = random.randint(1000000000, 9999999999)
    address = fake.address()
    day = fake.day_of_month()
    month = fake.month_name()
    year = fake.year()
    fakedate = f'{day} {month} {year}'
    randomDigit2 = str(random.randint(1, 3))
    NameSur = f'{firstName} {lastName}'
    date = f'{day} {month},{year}'
    return firstName, lastName, email, randomDigit, phone, address, fakedate, day, month, year, randomDigit2, NameSur, date

def user_login():
    return {'username':f'{fake.profile()["username"]}test{fake.word()}{str(random.randint(1, 3))}',
            'firstName':f'{fake.word()}{fake.word()}',
            'lastname': f'{fake.word()}{fake.word()}',
            'password': 'Password1!'
            }

user = user_login()
print(user['username'])