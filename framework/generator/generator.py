from os import path
from random import randint
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
    )


def generated_file():
    file_path = f'filetest{randint(0, 999)}.txt'
    with open(file_path, 'w+') as file:
        file.write(f'Hello, world!{randint(0, 999)}')
    return file.name, path.abspath(file_path)
