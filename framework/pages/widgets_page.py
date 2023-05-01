"""Module contains tests for Widgets tab on the site.

Contains page objects for:
Accordian,
"""
from random import sample, randint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from ..locators import AccordianPageLocators, AutoCompletePageLocators
from ..generator import generated_color


class AccordianPage(BasePage):
    """Accordian page object."""
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_order: str) -> tuple[str, str]:
        """Recieve accordian order: 'first', 'second', 'third'.
        \nReturns section title, section content."""
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
        Removes all colors
        :return: quantity of colors in multiple input
        """
        try:
            return len(self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS))
        except TimeoutException:
            return 0

    def clear_multiple_input(self):
        """
        Removes all colors from multiple input
        :return:
        """
        clear_button = self.element_is_clickable(self.locators.MULTIPLE_INPUT_CLEAR_BUTTON)
        clear_button.click()

    def check_colors_in_multiple_input(self) -> list[str]:
        """
        Checks colors in multiple input.
        :return: colors in multiple input
        """
        colors = self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS)
        colors_in_multiple_input = []
        for color in colors:
            colors_in_multiple_input.append(color.text)
        return colors_in_multiple_input
