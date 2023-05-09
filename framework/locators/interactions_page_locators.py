"""This module contains locators for Interactions tab on the site.

Contains locators for following tabs:
Sortable,
Selectable
"""
from selenium.webdriver.common.by import By


class SortablePageLocators:
    """Class for Sortable page locators."""
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    ITEMS_LIST = (By.CSS_SELECTOR, '.vertical-list-container .list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    ITEMS_GRID = (By.CSS_SELECTOR, '.create-grid .list-group-item')


class SelectablePageLocators:
    """Class for Selectable page locators."""
    TAB_LIST = (By.CSS_SELECTOR, '#demo-tab-list')
    ITEMS_LIST = (By.CSS_SELECTOR, '#verticalListContainer .list-group-item')
    ITEMS_LIST_ACTIVE = (By.CSS_SELECTOR, '#verticalListContainer .active')
    TAB_GRID = (By.CSS_SELECTOR, '#demo-tab-grid')
    ITEMS_GRID = (By.CSS_SELECTOR, '#gridContainer .list-group-item')
    ITEMS_GRID_ACTIVE = (By.CSS_SELECTOR, '#gridContainer .active')
