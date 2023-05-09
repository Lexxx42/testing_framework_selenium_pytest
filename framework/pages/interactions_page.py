"""Module contains page objects for Interactions tab on the site.

Contains tabs:
Sortable
"""
from random import sample
from .base_page import BasePage
from ..locators import SortablePageLocators


class SortablePage(BasePage):
    """Sortable page object."""
    locators = SortablePageLocators()

    def get_items_text_from_elements(self, elements) -> list[str]:
        """
        :returns: Texts of the items in elements list.
        """
        items = self.elements_are_present(elements)
        return [item.text for item in items]

    def get_items_of_list(self) -> list[str]:
        """:returns: Items of the list."""
        list_items = self.get_items_text_from_elements(self.locators.ITEMS_LIST)
        return list_items

    def get_items_of_grid(self) -> list[str]:
        """:returns: Items of the grid."""
        grid_items = self.get_items_text_from_elements(self.locators.ITEMS_GRID)
        return grid_items

    def change_list_order(self) -> None:
        """
        Changes the order of the items in the list.
        """
        self.change_order(self.locators.TAB_LIST, self.locators.ITEMS_LIST)

    def change_grid_order(self) -> None:
        """
        Changes the order of the items in the grid.
        """
        self.change_order(self.locators.TAB_GRID, self.locators.ITEMS_GRID)

    def change_order(self, tab_to_activate, elements_to_change_order):
        """
            Changes the order of the items in the elements. Within selected tab.
        """
        self.element_is_clickable(tab_to_activate).click()
        items_selected_to_change_order = sample(self.elements_are_visible(elements_to_change_order), k=2)
        item_which = items_selected_to_change_order[0]
        item_where = items_selected_to_change_order[-1]
        self.drag_and_drop_to_element(item_which, item_where)
