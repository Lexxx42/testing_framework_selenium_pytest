"""Module contains page objects for Interactions tab on the site.

Contains tabs:
Sortable,
Selectable,
Resizable
"""
from random import sample, randint
from .base_page import BasePage
from ..locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators


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


class SelectablePage(BasePage):
    """Selectable page object."""
    locators = SelectablePageLocators()

    def click_item_to_be_active(self, elements) -> None:
        """
        Click on the random item to be active.
        :param elements: Elements to select from.
        """
        items = self.elements_are_visible(elements)
        selected_item = sample(items, k=1)[0]
        selected_item.click()

    def activate_list_item(self) -> None:
        """Activates list item."""
        self.activate_item(self.locators.TAB_LIST, self.locators.ITEMS_LIST)

    def activate_grid_item(self) -> None:
        """Activates grid item."""
        self.activate_item(self.locators.TAB_GRID, self.locators.ITEMS_GRID)

    def activate_item(self, tab_to_activate, elements_to_activate_from) -> None:
        """
        Activates item from elements.
        :param tab_to_activate: The tab to activate.
        :param elements_to_activate_from: Elements to activate from.
        """
        self.element_is_clickable(tab_to_activate).click()
        self.click_item_to_be_active(elements_to_activate_from)

    def get_active_item_text(self, elements_to_search_for_active) -> str:
        """:returns: The active item from elements."""
        active_item = self.element_is_visible(elements_to_search_for_active)
        return active_item.text

    def get_active_list_item_text(self) -> str:
        """:returns: The active item from list."""
        return self.get_active_item_text(self.locators.ITEMS_LIST_ACTIVE)

    def get_active_grid_item_text(self) -> str:
        """:returns: The active item from grid."""
        return self.get_active_item_text(self.locators.ITEMS_GRID_ACTIVE)


class ResizablePage(BasePage):
    """Resizable page object."""
    locators = ResizablePageLocators()

    def get_px_from_width_and_height(self, size) -> tuple[int, int]:
        """
        Get the width and height of element.
        :returns: Height and width of element.
        """
        elements = size.split(';')
        width = elements[0].split(':')[-1].strip(' px')
        height = elements[1].split(':')[-1].strip(' px')
        return int(height), int(width)

    def get_width_and_height_of_element(self, element) -> str:
        """
        Get style attribute of element with height and width.
        :returns: Size of element.
        """
        element_size_from = self.element_is_visible(element)
        size = element_size_from.get_attribute('style')
        return size

    def change_size_of_element(self, element, width: int, height: int) -> None:
        """
        Changes size of element.
        :param element: Element to change size of.
        :param width: Width of element to change size to.
        :param height: Height of element to change size to.
        """
        self.drag_and_drop_by_offset(self.element_is_present(element), width, height)

    def change_size_resizable_box_greater_than_max_size(self) -> None:
        """Changes size of resizable box greater than maximum size."""
        self.change_size_of_element(self.locators.RESIZABLE_BOX_HANDLER, 600, 400)

    def change_size_resizable_box_lower_than_min_size(self) -> None:
        """Changes size of resizable box lower than minimum size."""
        self.change_size_of_element(self.locators.RESIZABLE_BOX_HANDLER, -500, -300)

    def change_size_resizable(self) -> None:
        """Changes size of resizable."""
        self.change_size_of_element(self.locators.RESIZABLE_HANDLER, randint(-50, 300), randint(-50, 300))

    def change_size_resizable_lower_zero(self):
        """Changes size of resizable lower than zero."""
        self.change_size_of_element(self.locators.RESIZABLE_HANDLER, -201, -201)

    def get_size_of_element(self, element) -> tuple[int, int]:
        """Get height and width of element."""
        size = self.get_px_from_width_and_height(self.get_width_and_height_of_element(element))
        return size

    def get_size_resizable_box(self) -> tuple[int, int]:
        """Get height and width of resizable box."""
        size_of_resizable_box = self.get_size_of_element(self.locators.RESIZABLE_BOX)
        return size_of_resizable_box

    def get_size_resizable(self) -> tuple[int, int]:
        """Get height and width of resizable."""
        size_of_resizable = self.get_size_of_element(self.locators.RESIZABLE)
        return size_of_resizable
