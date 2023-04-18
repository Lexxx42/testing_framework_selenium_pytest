from selenium.webdriver.common.by import By
from random import randint


class PracticeFormLocators:
    # form fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    GENDER_RADIOBUTTON = (By.CSS_SELECTOR, f'[for=\'gender-radio-{randint(1, 3)}\']')
    MOBILE_INPUT = (By.CSS_SELECTOR, '#userNumber')
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, '#dateOfBirthInput')
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
    RESULT_TABLE = (By.CSS_SELECTOR, '')
