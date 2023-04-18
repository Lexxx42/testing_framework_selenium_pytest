from ..locators import PracticeFormLocators
from ..generator import generated_person, generated_file, generated_subject
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time

class PracticeFormPage(BasePage):
    locators = PracticeFormLocators

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIOBUTTON).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(generated_subject())
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        time.sleep(4)

