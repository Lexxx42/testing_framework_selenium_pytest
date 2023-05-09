"""Module contains page objects for Interactions tab on the site.

Contains tabs:
Sortable
"""
from .base_page import BasePage
from ..locators import SortablePageLocators


class SortablePage(BasePage):
    """Sortable page object."""
    locators = SortablePageLocators()
