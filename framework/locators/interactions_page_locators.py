"""This module contains locators for Interactions tab on the site.

Contains locators for following tabs:
Sortable
"""
from selenium.webdriver.common.by import By


class SortablePageLocators:
    """Class for Sortable page locators."""
    FIRST_SECTION = (By.CSS_SELECTOR, '#section1Heading')
