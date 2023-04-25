"""Module contains tests for Widgets tab on the site.

Contains page objects for:
Accordian,
"""
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from ..locators import AccordianPageLocators


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
