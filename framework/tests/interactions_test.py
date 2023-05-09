"""Module contains tests for Interactions tab on the site.

Contains tabs:
Sortable,
Selectable,
Resizable
"""
from ..pages import SortablePage, SelectablePage, ResizablePage


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

    class TestResizablePage:
        """Class represents Resizable tab tests."""
        resizable_page_link = 'https://demoqa.com/resizable'

        def test_starting_size_of_resizable_box_is_200x200(self, driver):
            """Test starting size of resizable box."""
            resizable_page = ResizablePage(driver, self.resizable_page_link)
            resizable_page.open()
            current_height, current_width = resizable_page.get_size_resizable_box()
            starting_height = 200
            starting_width = 200
            assert current_height == starting_height, \
                f'Expected current height to be {starting_height}.' \
                f'Got {current_height}'
            assert current_width == starting_width, \
                f'Expected current height to be {starting_width}.' \
                f'Got {current_width}'

        def test_min_size_of_resizable_box_is_150x150(self, driver):
            """Test min size of resizable box."""
            resizable_page = ResizablePage(driver, self.resizable_page_link)
            resizable_page.open()
            resizable_page.change_size_resizable_box_lower_than_min_size()
            current_height, current_width = resizable_page.get_size_resizable_box()
            min_height = 150
            min_width = 150
            assert current_height == min_height, \
                f'Expected current height to be {min_height}.' \
                f'Got {current_height}'
            assert current_width == min_width, \
                f'Expected current height to be {min_width}.' \
                f'Got {current_width}'

        def test_max_size_of_resizable_box_is_500x300(self, driver):
            """Test max size of resizable box."""
            resizable_page = ResizablePage(driver, self.resizable_page_link)
            resizable_page.open()
            resizable_page.change_size_resizable_box_greater_than_max_size()
            current_height, current_width = resizable_page.get_size_resizable_box()
            max_height = 300
            max_width = 500
            assert current_height == max_height, \
                f'Expected current height to be {max_height}.' \
                f'Got {current_height}'
            assert current_width == max_width, \
                f'Expected current height to be {max_width}.' \
                f'Got {current_width}'

        def test_min_size_of_resizable_is_20x20(self, driver):
            """Test min size of resizable."""
            resizable_page = ResizablePage(driver, self.resizable_page_link)
            resizable_page.open()
            resizable_page.change_size_resizable_lower_zero()
            current_height, current_width = resizable_page.get_size_resizable()
            min_height = 20
            min_width = 20
            assert current_height == min_height, \
                f'Expected current height to be {min_height}.' \
                f'Got {current_height}'
            assert current_width == min_width, \
                f'Expected current height to be {min_width}.' \
                f'Got {current_width}'

        def test_size_of_resizable_can_be_changed(self, driver):
            """Test size of resizable can be changed."""
            resizable_page = ResizablePage(driver, self.resizable_page_link)
            resizable_page.open()
            starting_height, starting_width = resizable_page.get_size_resizable()
            resizable_page.change_size_resizable()
            current_height, current_width = resizable_page.get_size_resizable()
            assert starting_height != current_height, \
                f'Expected {current_height=} to be different from {starting_height=}.'
            assert starting_width != current_width, \
                f'Expected {current_width=} to be different from {starting_width=}.'
