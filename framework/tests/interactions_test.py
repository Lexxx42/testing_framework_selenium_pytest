"""Module contains tests for Interactions tab on the site.

Contains tabs:
Sortable,
Selectable
"""
from ..pages import SortablePage, SelectablePage


class TestInteractionsPage:
    """Class represents Widgets tab.
    Sortable
    """

    class TestSortablePage:
        """Class represents Sortable tab tests."""
        sortable_page_link = 'https://demoqa.com/sortable'

        def test_order_of_list_can_be_changed(self, driver):
            """Test order of list can be changed."""
            sortable_page = SortablePage(driver, self.sortable_page_link)
            sortable_page.open()
            order_of_list_before = sortable_page.get_items_of_list()
            sortable_page.change_list_order()
            order_of_list_after = sortable_page.get_items_of_list()
            assert order_of_list_before != order_of_list_after, \
                'Expected order of list to be different.' \
                f'Order before: {order_of_list_before}' \
                f'Order after: {order_of_list_after}'

        def test_order_of_grid_can_be_changed(self, driver):
            """Test order of grid can be changed."""
            sortable_page = SortablePage(driver, self.sortable_page_link)
            sortable_page.open()
            order_of_grid_before = sortable_page.get_items_of_grid()
            sortable_page.change_grid_order()
            order_of_grid_after = sortable_page.get_items_of_grid()
            assert order_of_grid_before != order_of_grid_after, \
                'Expected order of list to be different.' \
                f'Order before: {order_of_grid_before}' \
                f'Order after: {order_of_grid_after}'

    class TestSelectablePage:
        """Class represents Selectable tab tests."""
        selectable_page_link = 'https://demoqa.com/selectable'

        def test_list_item_can_be_activated(self, driver):
            """Test list item can be activated."""
            selectable_page = SelectablePage(driver, self.selectable_page_link)
            selectable_page.open()
            selectable_page.activate_list_item()
            activated_list_item = selectable_page.get_active_list_item_text()
            assert len(activated_list_item) > 0, \
                'Expected text from activated list item. ' \
                f'Got: {activated_list_item}'

        def test_grid_item_can_be_activated(self, driver):
            """Test grid item can be activated."""
            selectable_page = SelectablePage(driver, self.selectable_page_link)
            selectable_page.open()
            selectable_page.activate_grid_item()
            activated_grid_item = selectable_page.get_active_grid_item_text()
            assert len(activated_grid_item) > 0, \
                'Expected text from activated grid item. ' \
                f'Got: {activated_grid_item}'
