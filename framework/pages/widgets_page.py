"""Module contains tests for Widgets tab on the site.

Contains page objects for:
Accordian,
Auto Complete,
Date Picker,
Slider,
ProgressBarPage
"""
from random import sample, randint, choice
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from ..generator import generated_color, generated_date
from ..locators import AccordianPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators


class AccordianPage(BasePage):
    """Accordian page object."""
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_order: str) -> tuple[str, str]:
        """
        Receive accordian order: 'first', 'second', 'third'.
        \nReturns section title, section content.
        :returns: Text of section title and section content.
        """
        accordian = {
            'first': {
                'title': self.locators.FIRST_SECTION,
                'content': self.locators.FIRST_SECTION_TEXT
            },
            'second': {
                'title': self.locators.SECOND_SECTION,
                'content': self.locators.SECOND_SECTION_TEXT
            },
            'third': {
                'title': self.locators.THIRD_SECTION,
                'content': self.locators.THIRD_SECTION_TEXT
            }
        }
        section_title = self.element_is_clickable(accordian[accordian_order]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_order]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_order]['content']).text
        return section_title.text, section_content


class AutoCompletePage(BasePage):
    """Auto Complete page object."""
    locators = AutoCompletePageLocators()

    def fill_multiple_input(self) -> list[str]:
        """
        Fill multiple input with random from 2 to 5 available colors.
        :returns: Colors generated object.
        """
        colors = sample(next(generated_color()).color_name, k=randint(2, 5))
        for color in colors:
            multiple_input = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
            multiple_input.send_keys(color)
            multiple_input.send_keys(Keys.ENTER)
        return colors

    def remove_single_color_from_multiple_input(self) -> None:
        """
        Removes 1 color from selected colors in multiple input.
        """
        remove_buttons = self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEM_DELETE)
        for remove_button in remove_buttons:
            remove_button.click()
            break

    def count_colors_in_multiple_input(self) -> int:
        """
        Removes all colors.
        :returns: Quantity of colors in multiple input.
        """
        try:
            return len(self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS))
        except TimeoutException:
            return 0

    def clear_multiple_input(self) -> None:
        """
        Removes all colors from multiple input.
        """
        clear_button = self.element_is_clickable(self.locators.MULTIPLE_INPUT_CLEAR_BUTTON)
        clear_button.click()

    def check_colors_in_multiple_input(self) -> list[str]:
        """
        Checks colors in multiple input.
        :returns: Colors present in multiple input.
        """
        colors = self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS)
        colors_in_multiple_input = []
        for color in colors:
            colors_in_multiple_input.append(color.text)
        return colors_in_multiple_input

    def fill_single_input(self) -> str:
        """
        Fill single input with random color.
        :returns: Color entered in input.
        """
        color = sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_single_input(self) -> str:
        """
        Check color in single input.
        :return: Color present in single input.
        """
        color_in_single_input = self.element_is_visible(self.locators.SINGLE_INPUT_ITEM)
        return color_in_single_input.text


class DatePickerPage(BasePage):
    """Date Picker page object."""
    locators = DatePickerPageLocators()

    def select_date_only_from_picker(self) -> tuple[str, str]:
        """
        Select date from picker
        :returns: date before and after selection from date picker.
        """
        date = next(generated_date())
        input_date = self.element_is_clickable(self.locators.DATE_INPUT)
        value_date_before_selection = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_MONTH_SELECT, date.month)
        self.select_date_by_text(self.locators.DATE_YEAR_SELECT, date.year)
        self.select_element_from_elements_by_text(self.locators.DATE_AVAILABLE_DAYS, date.day)
        value_date_after_selection = input_date.get_attribute('value')
        return value_date_before_selection, value_date_after_selection

    def select_date_and_time(self) -> tuple[str, str]:
        """
        Select date and time from picker
        :returns: date before and after selection from date and time picker.
        """
        date = next(generated_date())
        input_date = self.element_is_clickable(self.locators.DATE_AND_TIME_INPUT)
        value_date_before_selection = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH_VIEW).click()
        self.select_element_from_elements_by_text(
            self.locators.DATE_AND_TIME_AVAILABLE_MONTHS, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR_VIEW).click()
        available_years = self.elements_are_visible(
            self.locators.DATE_AND_TIME_AVAILABLE_YEARS)
        choice(available_years).click()
        self.select_element_from_elements_by_text(self.locators.DATE_AVAILABLE_DAYS, date.day)
        self.select_element_from_elements_by_text(
            self.locators.DATE_AND_TIME_AVAILABLE_TIMES, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after_selection = input_date_after.get_attribute('value')
        return value_date_before_selection, value_date_after_selection


class SliderPage(BasePage):
    """Slider page object."""
    locators = SliderPageLocators()

    def change_slider_value(self):
        """
        Changes slider value.
        :returns: Value before and after change.
        """
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.drag_and_drop_by_offset(slider_input, randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        if value_after == 25:  # Default slider value.
            self.drag_and_drop_by_offset(slider_input, 26, 0)
            value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    """Progress Bar page object."""
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        """
        Changes the progress bar value.
        :returns: Value before and after change.
        """
        import time
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        start_stop_button = self.element_is_clickable(self.locators.START_STOP_BUTTON)
        start_stop_button.click()
        time.sleep(randint(2, 4))
        start_stop_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after
