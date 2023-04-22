from os import remove
from random import randint, choice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from ..locators import PracticeFormLocators
from ..generator import generated_person, generated_file, generated_subject, generated_state_and_city


class PracticeFormPage(BasePage):
    locators = PracticeFormLocators

    def fill_form_fields(self):
        try:
            self.remove_footer()
            person = next(generated_person())
            file_name, path = generated_file()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
            self.element_is_clickable(self.locators.GENDER_RADIOBUTTON).click()
            self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
            subject = generated_subject()
            self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
            self.element_is_clickable(self.locators.HOBBIES).click()
            self.element_is_clickable(self.locators.DATE_OF_BIRTH_SELECT).click()
            date_of_birth_month_select = Select(self.element_is_visible(self.locators.DATE_OF_BIRTH_MONTH_DROPDOWN))
            month_of_birth = randint(0, 11)
            date_of_birth_month_select.select_by_value(f'{month_of_birth}')
            date_of_birth_year_select = Select(self.element_is_visible(self.locators.DATE_OF_BIRTH_YEAR_DROPDOWN))
            year_of_birth = randint(1900, 2100)
            date_of_birth_year_select.select_by_value(f'{year_of_birth}')
            list_of_days = self.elements_are_visible(self.locators.DATE_OF_BIRTH_DAY_LIST)
            date_of_birth_day_element = choice(list_of_days)
            day_of_birth = date_of_birth_day_element.text
            date_of_birth_day_element.click()
            self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
            self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
            state, city = generated_state_and_city()
            self.element_is_clickable(self.locators.STATE_SELECT).click()
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
            self.element_is_clickable(self.locators.CITY_SELECT).click()
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
            self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        finally:
            remove(path)
        return person, (day_of_birth, month_of_birth, year_of_birth), subject

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
