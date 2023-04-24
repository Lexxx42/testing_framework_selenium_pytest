"""This module contains locators for Forms tab on the site.

Contains locators for following tabs:
PracticeForm.
"""
from random import randint
from selenium.webdriver.common.by import By


class PracticeFormLocators:
    """Class for Practice Form page locators."""
    # form fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    GENDER_RADIOBUTTON = (By.CSS_SELECTOR, f'[for=\'gender-radio-{randint(1, 3)}\']')
    MOBILE_INPUT = (By.CSS_SELECTOR, '#userNumber')

    # date of birth calendar
    DATE_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '#dateOfBirthInput')
    DATE_OF_BIRTH_MONTH_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    DATE_OF_BIRTH_YEAR_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    DATE_OF_BIRTH_DAY_LIST = (By.CSS_SELECTOR, '[role=\'option\']')

    SUBJECTS = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'[for=\'hobbies-checkbox-{randint(1, 3)}\']')
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, '#currentAddress')

    STATE_SELECT = (By.CSS_SELECTOR, '#state')
    STATE_INPUT = (By.CSS_SELECTOR, '#react-select-3-input')
    CITY_SELECT = (By.CSS_SELECTOR, '#city')
    CITY_INPUT = (By.CSS_SELECTOR, '#react-select-4-input')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    # table results
    RESULT_TABLE = (By.XPATH, '//div[@class=\'table-responsive\']//td[2]')
