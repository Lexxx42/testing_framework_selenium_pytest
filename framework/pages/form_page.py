from ..locators import PracticeFormLocators
from ..generator import generated_person, generated_file, generated_subject
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint, choice
import time


class PracticeFormPage(BasePage):
    locators = PracticeFormLocators

    def fill_form_fields(self):
        person = next(generated_person())
        # file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIOBUTTON).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(generated_subject())
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.DATE_OF_BIRTH_SELECT).click()
        date_of_birth_month_select = Select(self.element_is_visible(self.locators.DATE_OF_BIRTH_MONTH_DROPDOWN))
        date_of_birth_month_select.select_by_value(f'{randint(0, 11)}')
        date_of_birth_year_select = Select(self.element_is_visible(self.locators.DATE_OF_BIRTH_YEAR_DROPDOWN))
        date_of_birth_year_select.select_by_value(f'{randint(1900, 2100)}')
        list_of_days = self.elements_are_visible(self.locators.DATE_OF_BIRTH_DAY_LIST)
        choice(list_of_days).click()
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
        self.element_is_visible(self.locators.STATE_SELECT).click()


        time.sleep(5)
