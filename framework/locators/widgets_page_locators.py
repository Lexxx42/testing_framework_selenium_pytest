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


class AutoCompletePageLocators:
    """Class for Auto Complete page locators."""
    MULTIPLE_INPUT = (By.CSS_SELECTOR, '#autoCompleteMultipleInput')
    MULTIPLE_INPUT_ITEMS = (By.CSS_SELECTOR, '.auto-complete__multi-value')
    MULTIPLE_INPUT_ITEM_DELETE = (By.CSS_SELECTOR, '.auto-complete__multi-value path')
    MULTIPLE_INPUT_CLEAR_BUTTON = (By.CSS_SELECTOR, '.auto-complete__clear-indicator')

    SINGLE_INPUT = (By.CSS_SELECTOR, '#autoCompleteSingleInput')
    SINGLE_INPUT_ITEM = (By.CSS_SELECTOR, '.css-1uccc91-singleValue')
