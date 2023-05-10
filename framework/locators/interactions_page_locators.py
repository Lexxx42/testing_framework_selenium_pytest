"""This module contains locators for Interactions tab on the site.

Contains locators for following tabs:
Sortable,
Selectable,
Resizable,
Droppable
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


class ResizablePageLocators:
    """Class for Selectable page locators."""
    RESIZABLE_BOX = (By.CSS_SELECTOR, '#resizableBoxWithRestriction')
    RESIZABLE_BOX_HANDLER = (By.CSS_SELECTOR,
                             '#resizableBoxWithRestriction .react-resizable-handle')
    RESIZABLE = (By.CSS_SELECTOR, '#resizable')
    RESIZABLE_HANDLER = (By.CSS_SELECTOR, '#resizable .react-resizable-handle')


class DroppablePageLocators:
    """Class for Droppable page locators."""
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-simple')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, '#draggable')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '.simple-drop-container #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, '#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, '#notAcceptable')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '.accept-drop-container #droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-preventPropogation')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#dragBox')

    INNER_DROPPABLE_NOT_GREEDY = (By.CSS_SELECTOR, '#notGreedyInnerDropBox')
    INNER_DROPPABLE_NOT_GREEDY_TEXT = (By.CSS_SELECTOR, '#notGreedyInnerDropBox>p')
    OUTER_DROPPABLE_NOT_GREEDY_TEXT = (By.CSS_SELECTOR, '#notGreedyDropBox>p')

    INNER_DROPPABLE_GREEDY = (By.CSS_SELECTOR, '#greedyDropBoxInner')
    INNER_DROPPABLE_GREEDY_TEXT = (By.CSS_SELECTOR, '#greedyDropBoxInner>p')
    OUTER_DROPPABLE_GREEDY_TEXT = (By.CSS_SELECTOR, '#greedyDropBox>p')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, '#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, '#notRevertable')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '.revertable-drop-container #droppable')
