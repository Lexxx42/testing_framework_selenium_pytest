"""Module contains tests for Forms tab on the site.

Contains page objects for:
Practice Form.
"""
from os import remove
from random import randint, choice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from ..locators import PracticeFormLocators
from ..generator import generated_person, \
    generated_file, generated_subject, generated_state_and_city


class PracticeFormPage(BasePage):
    """Practice Form page object."""
    locators = PracticeFormLocators

    def fill_form_fields(self) -> tuple:
        """
        Fills all form fields.
        :returns: generated person object,
            (day, month, year of birth), subject.
        """
        _, path = generated_file()
        try:
            self.remove_footer()
            person = next(generated_person())
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
            self.element_is_clickable(self.locators.GENDER_RADIOBUTTON).click()
            self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
            subject = self.fill_subject_in_form()
            self.element_is_clickable(self.locators.HOBBIES).click()
            day_of_birth, month_of_birth, year_of_birth = self.fill_date_of_birth_in_form()
            self.element_is_visible(
                self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
            self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
            self.fill_state_and_city_in_form()
            self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        finally:
            remove(path)
        return person, (day_of_birth, month_of_birth, year_of_birth), subject

    def fill_date_of_birth_in_form(self) -> tuple[str, str, str]:
        """
        Fills day, month and year of birth in form.
        :returns: day, month and year of birth.
        """
        self.element_is_clickable(self.locators.DATE_OF_BIRTH_SELECT).click()
        date_of_birth_month_select = Select(
            self.element_is_visible(self.locators.DATE_OF_BIRTH_MONTH_DROPDOWN))
        month_of_birth = randint(0, 11)
        date_of_birth_month_select.select_by_value(f'{month_of_birth}')
        date_of_birth_year_select = Select(
            self.element_is_visible(self.locators.DATE_OF_BIRTH_YEAR_DROPDOWN))
        year_of_birth = randint(1900, 2100)
        date_of_birth_year_select.select_by_value(f'{year_of_birth}')
        list_of_days = self.elements_are_visible(self.locators.DATE_OF_BIRTH_DAY_LIST)
        date_of_birth_day_element = choice(list_of_days)
        day_of_birth = date_of_birth_day_element.text
        date_of_birth_day_element.click()
        return day_of_birth, str(month_of_birth), str(year_of_birth)

    def fill_state_and_city_in_form(self) -> None:
        """Fills state and city in form."""
        state, city = generated_state_and_city()
        self.element_is_clickable(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        self.element_is_clickable(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)

    def fill_subject_in_form(self) -> str:
        """
        Fill subject in the form.
        :returns: Subject generated.
        """
        subject = generated_subject()
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        return subject

    def check_form_results(self) -> list[str]:
        """
        Returns filled form fields.
        :returns: List of filled form fields.
        """
        form_result_fields = self.elements_are_visible(self.locators.RESULT_TABLE)
        filled_form_fields = []
        for field in form_result_fields:
            self.go_to_element(field)
            filled_form_fields.append(field.text)
        return filled_form_fields
