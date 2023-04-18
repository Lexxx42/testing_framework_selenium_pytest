from os import path
from random import randint, choice
from faker import Faker
from ..data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=randint(10, 80),
        salary=randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    file_path = f'filetest{randint(0, 999)}.txt'
    with open(file_path, 'w+') as file:
        file.write(f'Hello, world!{randint(0, 999)}')
    return file.name, path.abspath(file_path)


def generated_subject():
    available_subjects = ['Hindi', 'English', 'Maths', 'Physics',
                          'Chemistry', 'Biology', 'Computer Science',
                          'Commerce', 'Accounting', 'Economics', 'Arts',
                          'Social Studies', 'History', 'Civics']
    return choice(available_subjects)
