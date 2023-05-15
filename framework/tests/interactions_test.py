"""Module contains tests for Interactions tab on the site.

Contains tabs:
Sortable,
Selectable,
Resizable,
Droppable,
Draggable.
"""
import pytest
import allure
from ..pages import SortablePage, SelectablePage, ResizablePage, DroppablePage, \
    DraggablePage


@allure.suite('Alerts Interactions tab')
class TestInteractions:
    """Class represents Widgets tab.
    Sortable
    Selectable,
    Resizable,
    Droppable
    """
    text_dropped = 'Dropped!'

    @allure.feature('Sortable')
    class TestSortable:
        """Class represents Sortable tab tests."""
        sortable_page_link = 'https://demoqa.com/sortable'

        @allure.title('Test order of list can be changed.')
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

        @allure.title('Test order of grid can be changed.')
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

    @allure.feature('Selectable')
    class TestSelectable:
        """Class represents Selectable tab tests."""
        selectable_page_link = 'https://demoqa.com/selectable'

        @allure.title('Test list item can be activated.')
        def test_list_item_can_be_activated(self, driver):
            """Test list item can be activated."""
            selectable_page = SelectablePage(driver, self.selectable_page_link)
            selectable_page.open()
            selectable_page.activate_list_item()
            activated_list_item = selectable_page.get_active_list_item_text()
            assert len(activated_list_item) > 0, \
                'Expected text from activated list item. ' \
                f'Got: {activated_list_item}'

        @allure.title('Test grid item can be activated.')
        def test_grid_item_can_be_activated(self, driver):
            """Test grid item can be activated."""
            selectable_page = SelectablePage(driver, self.selectable_page_link)
            selectable_page.open()
            selectable_page.activate_grid_item()
            activated_grid_item = selectable_page.get_active_grid_item_text()
            assert len(activated_grid_item) > 0, \
                'Expected text from activated grid item. ' \
                f'Got: {activated_grid_item}'

    @allure.feature('Resizable')
    class TestResizable:
        """Class represents Resizable tab tests."""
        resizable_page_link = 'https://demoqa.com/resizable'

        @allure.title('Test starting size of resizable box.')
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

        @allure.title('Test min size of resizable box.')
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

        @allure.title('Test max size of resizable box.')
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

        @allure.title('Test min size of resizable.')
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

        @allure.title('Test size of resizable can be changed.')
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

    @allure.feature('Droppable')
    class TestDroppable:
        """Class represents Droppable tab tests."""
        droppable_page_link = 'https://demoqa.com/droppable'

        @allure.title('Test element changes text when element is dropped into it.')
        def test_simple_droppable(self, driver):
            """Test element changes text when element is dropped into it."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_simple_tab()
            droppable_page.drop_simple()
            drop_here_text = droppable_page.get_simple_drop_here_element_text()
            expected_drop_here_text = TestInteractions.text_dropped
            assert drop_here_text == expected_drop_here_text, \
                f'Expected droppable text to be {expected_drop_here_text}. ' \
                f'Got: {drop_here_text}'

        @allure.title('Test acceptable element is accepted by droppable.')
        def test_accept_droppable_acceptable_is_accepted(self, driver):
            """Test acceptable element is accepted by droppable."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_accept_tab()
            droppable_page.drop_accept_acceptable()
            drop_here_text = droppable_page.get_accept_drop_here_element_text()
            expected_drop_here_text = TestInteractions.text_dropped
            assert drop_here_text == expected_drop_here_text, \
                f'Expected droppable text to be {expected_drop_here_text}. ' \
                f'Got: {drop_here_text}'

        @allure.title('Test not acceptable element isn\'t accepted by droppable.')
        def test_accept_droppable_not_acceptable_is_not_accepted(self, driver):
            """Test not acceptable element isn't accepted by droppable."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_accept_tab()
            droppable_page.drop_accept_not_acceptable()
            drop_here_text = droppable_page.get_accept_drop_here_element_text()
            expected_drop_here_text = 'Drop here'
            assert drop_here_text == expected_drop_here_text, \
                f'Expected droppable text to be {expected_drop_here_text}. ' \
                f'Got: {drop_here_text}'

        @allure.title('Test drop element into not greedy inner '
                      'changes both inner and outer elements.')
        def test_prevent_propogation_droppable_not_greedy(self, driver):
            """Test drop element into not greedy inner changes both inner and outer elements."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_prevent_propogation_tab()
            droppable_page.drop_prevent_propogation_not_greedy_inner()
            outer_droppable_text = \
                droppable_page.get_prevent_propogation_outer_droppable_not_greedy_text()
            inner_droppable_text = \
                droppable_page.get_prevent_propogation_inner_droppable_not_greedy_text()
            expected_outer_droppable_text = TestInteractions.text_dropped
            expected_inner_droppable_text = TestInteractions.text_dropped
            assert outer_droppable_text == expected_outer_droppable_text, \
                f'Expected outer droppable text to be {expected_outer_droppable_text}. ' \
                f'Got: {outer_droppable_text}'
            assert inner_droppable_text == expected_inner_droppable_text, \
                f'Expected inner droppable text to be {expected_inner_droppable_text}. ' \
                f'Got: {inner_droppable_text}'

        @allure.title('Test drop element into greedy inner changes only inner element.')
        def test_prevent_propogation_droppable_greedy(self, driver):
            """Test drop element into greedy inner changes only inner element."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_prevent_propogation_tab()
            droppable_page.drop_prevent_propogation_greedy_inner()
            outer_droppable_text = \
                droppable_page.get_prevent_propogation_outer_droppable_greedy_text()
            inner_droppable_text = \
                droppable_page.get_prevent_propogation_inner_droppable_greedy_text()
            expected_outer_droppable_text = 'Outer droppable'
            expected_inner_droppable_text = TestInteractions.text_dropped
            assert outer_droppable_text == expected_outer_droppable_text, \
                f'Expected outer droppable text to be {expected_outer_droppable_text}. ' \
                f'Got: {outer_droppable_text}'
            assert inner_droppable_text == expected_inner_droppable_text, \
                f'Expected inner droppable text to be {expected_inner_droppable_text}. ' \
                f'Got: {inner_droppable_text}'

        @allure.title('Test element Will Revert activates drop box.')
        def test_revert_draggable_droppable(self, driver):
            """Test element Will Revert activates drop box."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_revert_draggable_tab()
            droppable_page.drop_revert_draggable_will_revert()
            drop_here_text = droppable_page.get_revert_draggable_drop_here_element_text()
            expected_drop_here_text = TestInteractions.text_dropped
            assert drop_here_text == expected_drop_here_text, \
                f'Expected droppable text to be {expected_drop_here_text}. ' \
                f'Got: {drop_here_text}'

        @allure.title('Test element Not Revert activates drop box.')
        def test_not_revert_draggable_droppable(self, driver):
            """Test element Not Revert activates drop box."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_revert_draggable_tab()
            droppable_page.drop_revert_draggable_not_revert()
            drop_here_text = droppable_page.get_revert_draggable_drop_here_element_text()
            expected_drop_here_text = TestInteractions.text_dropped
            assert drop_here_text == expected_drop_here_text, \
                f'Expected droppable text to be {expected_drop_here_text}. ' \
                f'Got: {drop_here_text}'

        @allure.title('Test Will Revert returns to start position after dragging.')
        def test_revertable_draggable_will_return_to_current_position_after_dragging(self, driver):
            """Test Will Revert returns to start position after dragging."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_revert_draggable_tab()
            droppable_page.change_position_of_will_revert()
            revertable_start_position = droppable_page.get_position_of_will_revert()
            droppable_page.drop_revert_draggable_will_revert()
            is_reverted = droppable_page.is_will_revert_reverted_to_current_position(
                revertable_start_position)
            assert is_reverted is True, \
                'Expected Will Revert to return to current position after dragging.' \
                f'But got {is_reverted}'

        @allure.title('Test element Not Revert returns to dropbox.')
        def test_not_revertable_will_return_after_dragging_out_of_dropbox(self, driver):
            """Test element Not Revert returns to dropbox."""
            droppable_page = DroppablePage(driver, self.droppable_page_link)
            droppable_page.open()
            droppable_page.go_to_revert_draggable_tab()
            droppable_page.drop_revert_draggable_not_revert()
            not_revertable_start_position = droppable_page.get_position_of_not_revert()
            droppable_page.change_position_of_not_revert()
            is_reverted = droppable_page.is_not_revert_reverted_to_current_position(
                not_revertable_start_position)
            assert is_reverted is True, \
                'Expected Not Revert to return to current position after dragging.' \
                f'But got {is_reverted}'

    @allure.feature('Draggable')
    class TestDraggable:
        """Class represents Draggable tab tests."""
        draggable_page_link = 'https://demoqa.com/dragabble'

        @allure.title('Test element Drag me can be dragged.')
        def test_simple_draggable(self, driver):
            """Test element Drag me can be dragged."""
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_simple_tab()
            draggable_page.drag_simple_drag_me()
            left_coord_start, top_coord_start = \
                draggable_page.get_simple_drag_me_coordinates()
            draggable_page.drag_simple_drag_me()
            left_coord_after_drag, top_coord_after_drag = \
                draggable_page.get_simple_drag_me_coordinates()
            assert (left_coord_start, top_coord_start) != \
                   (left_coord_after_drag, top_coord_after_drag), \
                'Expected coordinates to change after drag.' \
                f'{left_coord_start=} {top_coord_start=}' \
                f'{left_coord_after_drag=} {top_coord_after_drag=}'

        @allure.title('Test element Only X can be dragged on x-axis.')
        def test_only_x_changes_coordinate_left_after_dragging_on_x_axis(self, driver):
            """Test element Only X can be dragged on x-axis."""
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_axis_restricted_tab()
            draggable_page.drag_only_x()
            left_coord_start, top_coord_start = \
                draggable_page.get_only_x_coordinates()
            draggable_page.drag_only_x()
            left_coord_after_drag, top_coord_after_drag = \
                draggable_page.get_only_x_coordinates()
            assert left_coord_start != left_coord_after_drag, \
                'Expected coordinate left to change after drag.' \
                f'{left_coord_start=} {top_coord_start=}' \
                f'{left_coord_after_drag=} {top_coord_after_drag=}'

        @allure.title('Test element Only X can\'t be dragged on y-axis.')
        def test_only_x_not_changes_coordinate_top_after_dragging_on_y_axis(self, driver):
            """Test element Only X can't be dragged on y-axis."""
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_axis_restricted_tab()
            draggable_page.drag_only_x()
            expected_top_coordinate = 0
            left_coord_start, top_coord_start = \
                draggable_page.get_only_x_coordinates()
            draggable_page.drag_only_x()
            left_coord_after_drag, top_coord_after_drag = \
                draggable_page.get_only_x_coordinates()
            assert top_coord_start == expected_top_coordinate, \
                'Expected coordinate top to not change after drag.' \
                f'And be {expected_top_coordinate=}' \
                f'{left_coord_start=} {top_coord_start=}'
            assert top_coord_after_drag == expected_top_coordinate, \
                'Expected coordinate top to not change after drag.' \
                f'And be {expected_top_coordinate=}' \
                f'{left_coord_after_drag=} {top_coord_after_drag=}'

        @allure.title('Test element Only Y can\'t be dragged on x-axis.')
        def test_only_y_not_changes_coordinate_left_after_dragging_on_x_axis(self, driver):
            """Test element Only Y can't be dragged on x-axis."""
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_axis_restricted_tab()
            draggable_page.drag_only_y()
            expected_left_coordinate = 0
            left_coord_start, top_coord_start = \
                draggable_page.get_only_y_coordinates()
            draggable_page.drag_only_y()
            left_coord_after_drag, top_coord_after_drag = \
                draggable_page.get_only_y_coordinates()
            assert left_coord_start == expected_left_coordinate, \
                'Expected coordinate top to not change after drag.' \
                f'And be {expected_left_coordinate=}' \
                f'{left_coord_start=} {top_coord_start=}'
            assert left_coord_after_drag == expected_left_coordinate, \
                'Expected coordinate top to not change after drag.' \
                f'And be {expected_left_coordinate=}' \
                f'{left_coord_after_drag=} {top_coord_after_drag=}'

        @allure.title('Test element Only Y can be dragged on y-axis.')
        def test_only_y_changes_coordinate_top_after_dragging_on_y_axis(self, driver):
            """Test element Only Y can be dragged on y-axis."""
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_axis_restricted_tab()
            draggable_page.drag_only_y()
            left_coord_start, top_coord_start = \
                draggable_page.get_only_y_coordinates()
            draggable_page.drag_only_y()
            left_coord_after_drag, top_coord_after_drag = \
                draggable_page.get_only_y_coordinates()
            assert top_coord_start != top_coord_after_drag, \
                'Expected coordinate top to change after drag.' \
                f'{left_coord_start=} {top_coord_start=}' \
                f'{left_coord_after_drag=} {top_coord_after_drag=}'

        @allure.title('Test element \'I\'m contained within the box\''
                      'can\'t be moved upper restricted container.')
        def test_box_can_not_be_moved_upper_restricted_container(self, driver):
            """
            Test element 'I'm contained within the box'
            can't be moved upper restricted container.
            """
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_container_restricted_tab()
            draggable_page.drag_box_upper_restricted_container()
            top_upper_restriction = 0
            left_coordinate, top_coordinate = \
                draggable_page.get_contained_withing_box_coordinates()
            assert top_coordinate == top_upper_restriction, \
                f'Expected top coordinate to be ' \
                f'container restricted and be {top_upper_restriction=}' \
                f'Got: {left_coordinate=} {top_coordinate=}'

        @allure.title('Test element \'I\'m contained within the box\''
                      'can\'t be moved lower restricted container.')
        def test_box_can_not_be_moved_lower_restricted_container(self, driver):
            """
            Test element 'I'm contained within the box'
            can't be moved lower restricted container.
            """
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_container_restricted_tab()
            draggable_page.drag_box_lower_restricted_container()
            top_lower_restriction = 106
            left_coordinate, top_coordinate = \
                draggable_page.get_contained_withing_box_coordinates()
            assert top_coordinate == top_lower_restriction, \
                f'Expected top coordinate to be ' \
                f'container restricted and be {top_lower_restriction=}' \
                f'Got: {left_coordinate=} {top_coordinate=}'

        @allure.title('Test element \'I\'m contained within the box\''
                      'can\'t be moved lefter restricted container.')
        def test_box_can_not_be_moved_lefter_restricted_container(self, driver):
            """
            Test element 'I'm contained within the box'
            can't be moved lefter restricted container.
            """
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_container_restricted_tab()
            draggable_page.drag_box_lefter_restricted_container()
            left_lefter_restriction = 0
            left_coordinate, top_coordinate = \
                draggable_page.get_contained_withing_box_coordinates()
            assert left_coordinate == left_lefter_restriction, \
                f'Expected top coordinate to be ' \
                f'container restricted and be {left_lefter_restriction=}' \
                f'Got: {left_coordinate=} {top_coordinate=}'

        @allure.title('Test element \'I\'m contained within the box\''
                      'can\'t be moved righter restricted container.')
        @pytest.mark.skip(reason='not implemented')
        def test_box_can_not_be_moved_righter_restricted_container(self, driver):
            """
            Test element 'I'm contained within the box'
            can't be moved righter restricted container.
            """
            draggable_page = DraggablePage(driver, self.draggable_page_link)
            draggable_page.open()
            draggable_page.go_to_container_restricted_tab()
            draggable_page.drag_box_righter_restricted_container()
            # TODO: how do i test it on adaptive interface?
