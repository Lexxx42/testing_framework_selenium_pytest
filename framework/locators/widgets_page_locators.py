"""This module contains locators for Widgets tab on the site.

Contains locators for following tabs:
Accordian,
"""
from selenium.webdriver.common.by import By


class AccordianPageLocators:
    """Class for Accordian page locators."""
    FIRST_SECTION = (By.CSS_SELECTOR, '#section1Heading')
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, '#section1Content p')

    SECOND_SECTION = (By.CSS_SELECTOR, '#section2Heading')
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, '#section2Content p')

    THIRD_SECTION = (By.CSS_SELECTOR, '#section3Heading')
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, '#section3Content p')
