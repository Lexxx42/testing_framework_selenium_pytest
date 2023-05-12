"""Module contains page objects for Interactions tab on the site.

Contains tabs:
Sortable,
Selectable,
Resizable,
Droppable,
Draggable
"""
from random import sample, randint
from .base_page import BasePage
from ..locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators


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
        items_selected_to_change_order = sample(
            self.elements_are_visible(elements_to_change_order), k=2)
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
        self.change_size_of_element(
            self.locators.RESIZABLE_HANDLER, randint(-50, 300), randint(-50, 300))

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


class DroppablePage(BasePage):
    """Droppable page object."""
    locators = DroppablePageLocators()

    def go_to_simple_tab(self) -> None:
        """Go to simple tab."""
        simple_tab = self.element_is_clickable(self.locators.SIMPLE_TAB)
        simple_tab.click()

    def go_to_accept_tab(self) -> None:
        """Go to accept tab."""
        accept_tab = self.element_is_clickable(self.locators.ACCEPT_TAB)
        accept_tab.click()

    def go_to_prevent_propogation_tab(self) -> None:
        """Go to prevent propogation tab."""
        prevent_propogation_tab = self.element_is_clickable(self.locators.PREVENT_TAB)
        prevent_propogation_tab.click()

    def go_to_revert_draggable_tab(self) -> None:
        """Go to revert draggable tab."""
        revert_draggable_tab = self.element_is_clickable(self.locators.REVERT_TAB)
        revert_draggable_tab.click()

    def drop_simple(self) -> None:
        """Drops drag element into drop element."""
        drag_me = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.drag_and_drop_to_element(drag_me, drop_here)

    def drop_accept_acceptable(self) -> None:
        """Drops drag Acceptable element into drop element."""
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.drag_and_drop_to_element(acceptable, drop_here)

    def drop_accept_not_acceptable(self) -> None:
        """Drops drag Not Acceptable element into drop element."""
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.drag_and_drop_to_element(not_acceptable, drop_here)

    def drop_prevent_propogation_not_greedy_inner(self) -> None:
        """Drops drag Drag Me element into not greedy inner."""
        drag_me = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner = self.element_is_visible(self.locators.INNER_DROPPABLE_NOT_GREEDY)
        self.drag_and_drop_to_element(drag_me, not_greedy_inner)

    def drop_prevent_propogation_greedy_inner(self) -> None:
        """Drops drag Drag Me element into greedy inner."""
        drag_me = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        greedy_inner = self.element_is_visible(self.locators.INNER_DROPPABLE_GREEDY)
        self.drag_and_drop_to_element(drag_me, greedy_inner)

    def drop_revert_draggable_will_revert(self) -> None:
        """Drops Will Revert element into Drop Here."""
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.drag_and_drop_to_element(will_revert, drop_here)

    def drop_revert_draggable_not_revert(self) -> None:
        """Drops Not Revert element into Drop Here."""
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.drag_and_drop_to_element(not_revert, drop_here)

    def get_simple_drop_here_element_text(self) -> str:
        """:returns: Drop here element text for Simple tab."""
        drop_here = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        return drop_here.text

    def get_accept_drop_here_element_text(self) -> str:
        """:returns: Drop here element text for Accept tab."""
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        return drop_here.text

    def get_prevent_propogation_outer_droppable_not_greedy_text(self) -> str:
        """:returns: Outer not greedy drappable text for Prevent Propogation tab."""
        outer_droppable_not_greedy = self.element_is_visible(
            self.locators.OUTER_DROPPABLE_NOT_GREEDY_TEXT)
        return outer_droppable_not_greedy.text

    def get_prevent_propogation_outer_droppable_greedy_text(self) -> str:
        """:returns: Outer greedy drappable text for Prevent Propogation tab."""
        outer_droppable_greedy = self.element_is_visible(self.locators.OUTER_DROPPABLE_GREEDY_TEXT)
        return outer_droppable_greedy.text

    def get_prevent_propogation_inner_droppable_not_greedy_text(self) -> str:
        """:returns: Inner not greedy drappable text for Prevent Propogation tab."""
        inner_droppable_not_greedy = self.element_is_visible(
            self.locators.INNER_DROPPABLE_NOT_GREEDY_TEXT)
        return inner_droppable_not_greedy.text

    def get_prevent_propogation_inner_droppable_greedy_text(self) -> str:
        """:returns: Inner greedy drappable text for Prevent Propogation tab."""
        inner_droppable_greedy = self.element_is_visible(self.locators.INNER_DROPPABLE_GREEDY_TEXT)
        return inner_droppable_greedy.text

    def get_revert_draggable_drop_here_element_text(self) -> str:
        """:returns: Drop here element text for Revert Draggable tab."""
        drop_here = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        return drop_here.text

    def get_position_of_will_revert(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of Will Revert.
        """
        return self.get_position_of_element(self.locators.WILL_REVERT)

    def get_position_of_not_revert(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of Not Revert.
        """
        return self.get_position_of_element(self.locators.NOT_REVERT)

    def __is_element_reverted_to_start_position(self, element_locator, start_position: str):
        """
        :param element_locator: Locator of element.
        :param start_position: Style attribute of element.
        :returns: True, if Revert reverted to start position.
        """
        locator = element_locator
        locator_positional = locator[1] + f'[style=\'{start_position}\']'
        locator_to_wait_for = (locator[0], locator_positional)
        return self.is_element_visible(locator_to_wait_for)

    def change_position_of_will_revert(self) -> None:
        """Change position of Will Revert."""
        will_revert = self.element_is_visible(self.locators.WILL_REVERT)
        self.drag_and_drop_by_offset(will_revert, 1, 1)

    def change_position_of_not_revert(self) -> None:
        """Change position of Not Revert."""
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        self.drag_and_drop_by_offset(not_revert, x_coordinate=300, y_coordinate=300)

    def is_will_revert_reverted_to_current_position(self, current_position) -> bool:
        """:returns: True if element is visible with current_position style."""
        return self.__is_element_reverted_to_start_position(
            self.locators.WILL_REVERT, current_position)

    def is_not_revert_reverted_to_current_position(self, current_position) -> bool:
        """:returns: True if element is visible with current_position style."""
        return self.__is_element_reverted_to_start_position(
            self.locators.NOT_REVERT, current_position)


class DraggablePage(BasePage):
    """Draggable page object."""
    locators = DraggablePageLocators()

    def go_to_simple_tab(self) -> None:
        """Go to simple tab."""
        simple_tab = self.element_is_clickable(self.locators.SIMPLE_TAB)
        simple_tab.click()

    def go_to_axis_restricted_tab(self) -> None:
        """Go to axis restricted tab."""
        axis_restricted_tab = self.element_is_clickable(self.locators.AXIS_RESTRICTED_TAB)
        axis_restricted_tab.click()

    def go_to_container_restricted_tab(self) -> None:
        """Go to container restricted tab."""
        container_restricted_tab = self.element_is_clickable(self.locators.CONTAINER_RESTRICTED_TAB)
        container_restricted_tab.click()

    def __drag_element_on_page(self, elements_locator):
        """Drag element on page."""
        element_to_drag = self.element_is_visible(elements_locator)
        coordinate_x = randint(-100, 250)
        coordinate_y = randint(-50, 250)
        self.drag_and_drop_by_offset(element_to_drag, coordinate_x, coordinate_y)

    def drag_simple_drag_me(self):
        """Drag Drag me element."""
        self.__drag_element_on_page(self.locators.DRAG_ME_SIMPLE)

    def drag_only_x(self):
        """Drag Only X element."""
        self.__drag_element_on_page(self.locators.ONLY_X)

    def drag_only_y(self):
        """Drag Only Y element."""
        self.__drag_element_on_page(self.locators.ONLY_Y)

    def __drag_contained_element_to_coordinate(
            self, elements_locator, coordinate_x=0, coordinate_y=0):
        """Drag element on page ith specific coordinates."""
        element_to_drag = self.element_is_visible(elements_locator)
        self.drag_and_drop_by_offset(element_to_drag, coordinate_x, coordinate_y)

    def drag_box_upper_restricted_container(self):
        """Drag box upper from restricted container."""
        self.__drag_contained_element_to_coordinate(
            self.locators.BOX_CONTENT, coordinate_y=randint(-50, -1))

    def drag_box_lower_restricted_container(self):
        """Drag box lower from restricted container."""
        self.__drag_contained_element_to_coordinate(
            self.locators.BOX_CONTENT, coordinate_y=randint(110, 200))

    def drag_box_lefter_restricted_container(self):
        """Drag box lefter from restricted container."""
        self.__drag_contained_element_to_coordinate(
            self.locators.BOX_CONTENT, coordinate_x=randint(-50, -1))

    def drag_box_righter_restricted_container(self):
        """Drag box righter from restricted container."""
        self.__drag_contained_element_to_coordinate(
            self.locators.BOX_CONTENT, coordinate_x=1000)

    def get_simple_drag_me_position(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of Drag me.
        """
        return self.get_position_of_element(self.locators.DRAG_ME_SIMPLE)

    def get_only_x_position(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of Only X.
        """
        return self.get_position_of_element(self.locators.ONLY_X)

    def get_only_y_position(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of Only Y.
        """
        return self.get_position_of_element(self.locators.ONLY_Y)

    def get_contained_withing_box_position(self) -> str:
        """
        Get position from style attribute of element.
        :returns: Position of I'm contained within the box.
        """
        return self.get_position_of_element(self.locators.BOX_CONTENT)

    def get_coordinates_of_element_from_position(self, position_style_attribute) -> tuple[int, int]:
        """
        Get coordinates from position style attribute of element.
        :returns: Left and top position.
        """
        elements = position_style_attribute.split(';')
        left = elements[1].split(':')[-1].strip(' px')
        top = elements[2].split(':')[-1].strip(' px')
        return int(left), int(top)

    def get_simple_drag_me_coordinates(self) -> tuple[int, int]:
        """
        Get coordinates from position style attribute of Drag me.
        :returns: Left and top position.
        """
        get_me_position = self.get_simple_drag_me_position()
        left_coordinate, top_coordinate = \
            self.get_coordinates_of_element_from_position(get_me_position)
        return left_coordinate, top_coordinate

    def get_only_x_coordinates(self) -> tuple[int, int]:
        """
        Get coordinates from position style attribute of Only X.
        :returns: Left and top position.
        """
        only_x_position = self.get_only_x_position()
        left_coordinate, top_coordinate = \
            self.get_coordinates_of_element_from_position(only_x_position)
        return left_coordinate, top_coordinate

    def get_only_y_coordinates(self) -> tuple[int, int]:
        """
        Get coordinates from position style attribute of Only Y.
        :returns: Left and top position.
        """
        only_y_position = self.get_only_y_position()
        left_coordinate, top_coordinate = \
            self.get_coordinates_of_element_from_position(only_y_position)
        return left_coordinate, top_coordinate

    def get_contained_withing_box_coordinates(self) -> tuple[int, int]:
        """
        Get coordinates from position style attribute of I'm contained within the box.
        :returns: Left and top position.
        """
        contained_withing_box_position = self.get_contained_withing_box_position()
        left_coordinate, top_coordinate = \
            self.get_coordinates_of_element_from_position(contained_withing_box_position)
        return left_coordinate, top_coordinate
