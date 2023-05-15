"""Module contains tests for Forms tab on the site.

Contains page objects for:
Practice Form.
"""
from os import remove
from random import randint, choice
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from ..locators import PracticeFormLocators
from ..generator import generated_person, \
    generated_file, generated_subject, generated_state_and_city


class PracticeFormPage(BasePage):
    """Practice Form page object."""
    locators = PracticeFormLocators

    @allure.step('Fills all form fields.')
    def fill_form_fields(self) -> tuple:
        """
        Fills all form fields.
        :returns: generated person object,
            (day, month, year of birth), subject.
        """
        with allure.step('Generate file and path to it'):
            _, path = generated_file()
        try:
            with allure.step('Removes footer from page to not interfere'):
                self.remove_footer()
            with allure.step('Generate person info'):
                person = next(generated_person())
            with allure.step('Enter persons first name'):
                self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
            with allure.step('Enter persons last name'):
                self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
            with allure.step('Enter persons email'):
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
            with allure.step('Click on gender radiobutton'):
                self.element_is_clickable(self.locators.GENDER_RADIOBUTTON).click()
            with allure.step('Enter persons mobile'):
                self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
            with allure.step('Enter persons subjects'):
                subject = self.fill_subject_in_form()
            with allure.step('Click on hobbies checkboxes'):
                self.element_is_clickable(self.locators.HOBBIES).click()
            with allure.step('Enter persons date of birth'):
                day_of_birth, month_of_birth, year_of_birth = self.fill_date_of_birth_in_form()
            with allure.step('Enter persons current address'):
                self.element_is_visible(
                    self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
            with allure.step('Enter persons file'):
                self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
            with allure.step('Enter persons state and city'):
                self.fill_state_and_city_in_form()
            with allure.step('Click on submit button'):
                self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        finally:
            remove(path)
        return person, (day_of_birth, month_of_birth, year_of_birth), subject

    @allure.step('Fills day, month and year of birth in form.')
    def fill_date_of_birth_in_form(self) -> tuple[str, str, str]:
        """
        Fills day, month and year of birth in form.
        :returns: day, month and year of birth.
        """
        with allure.step('Click on date of birth selector'):
            self.element_is_clickable(self.locators.DATE_OF_BIRTH_SELECT).click()

        with allure.step('Select month of birth'):
            date_of_birth_month_select = Select(
                self.element_is_visible(self.locators.DATE_OF_BIRTH_MONTH_DROPDOWN))
            month_of_birth = randint(0, 11)
            date_of_birth_month_select.select_by_value(f'{month_of_birth}')
        with allure.step('Select year of birth'):
            date_of_birth_year_select = Select(
                self.element_is_visible(self.locators.DATE_OF_BIRTH_YEAR_DROPDOWN))
            year_of_birth = randint(1900, 2100)
        with allure.step('Select day of birth'):
            date_of_birth_year_select.select_by_value(f'{year_of_birth}')
            list_of_days = self.elements_are_visible(self.locators.DATE_OF_BIRTH_DAY_LIST)
            date_of_birth_day_element = choice(list_of_days)
            day_of_birth = date_of_birth_day_element.text
            date_of_birth_day_element.click()
        return day_of_birth, str(month_of_birth), str(year_of_birth)

    @allure.step('Fills state and city in form.')
    def fill_state_and_city_in_form(self) -> None:
        """Fills state and city in form."""
        with allure.step('Generate couple of state and city'):
            state, city = generated_state_and_city()
        with allure.step('Click on select state'):
            self.element_is_clickable(self.locators.STATE_SELECT).click()
        with allure.step('Fill state'):
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        with allure.step('Click on select city'):
            self.element_is_clickable(self.locators.CITY_SELECT).click()
        with allure.step('Fill city'):
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)

    @allure.step('Fill subject in the form.')
    def fill_subject_in_form(self) -> str:
        """
        Fill subject in the form.
        :returns: Subject generated.
        """
        with allure.step('Generate subject'):
            subject = generated_subject()
        with allure.step('Fill subject'):
            self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        return subject

    @allure.step('Returns filled form fields.')
    def get_form_results(self) -> list[str]:
        """
        Returns filled form fields.
        :returns: Results of filled form fields.
        """
        form_result_fields = self.elements_are_visible(self.locators.RESULT_TABLE)
        filled_form_fields = []
        for field in form_result_fields:
            self.go_to_element(field)
            filled_form_fields.append(field.text)
        return filled_form_fields
