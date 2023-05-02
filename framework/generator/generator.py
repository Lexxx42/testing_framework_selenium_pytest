"""This module is used for generating data for tests."""
from os import path
from random import randint, choice
from faker import Faker
from ..data import Person, Color

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    """
    Generation person data with Faker library.
    :returns: person generator object.
    """
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


def generated_file() -> tuple[str, str]:
    """
    File generation.
    :returns: file name and absolute path.
    """
    file_path = f'filetest{randint(0, 999)}.txt'
    with open(file_path, 'w+', encoding='UTF-8') as file:
        file.write(f'Hello, world!{randint(0, 999)}')
    return file.name, path.abspath(file_path)


def generated_subject() -> str:
    """
    Subjects generation.
    :returns: random available subject.
    """
    available_subjects = ['Hindi', 'English', 'Maths', 'Physics',
                          'Chemistry', 'Biology', 'Computer Science',
                          'Commerce', 'Accounting', 'Economics', 'Arts',
                          'Social Studies', 'History', 'Civics']
    return choice(available_subjects)


def generated_state_and_city() -> tuple[str, str]:
    """
    Generation of pair state/city.
    :returns: random available state and city pair.
    """
    available_states_cities = {
        'NCR': ['Delhi', 'Gurgaon', 'Noida'],
        'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
        'Haryana': ['Karnal', 'Panipat'],
        'Rajasthan': ['Jaipur', 'Jaiselmer']
    }
    random_state = choice(list(available_states_cities.keys()))
    random_city = choice(available_states_cities[random_state])
    return random_state, random_city


def generated_color():
    """
    Generation of color.
    :returns: color generator object.
    """
    yield Color(
        color_name=[
            'Red', 'Blue', 'Green', 'Yellow',
            'Purple', 'Black', 'White',
            'Voilet', 'Indigo', 'Magenta', 'Aqua'
        ]
    )
