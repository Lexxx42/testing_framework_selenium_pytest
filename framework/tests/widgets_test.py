"""Module contains tests for Widgets tab on the site.

Contains tabs:
Accordian,
Auto Complete,
Date Picker,
Slider,
Progress Bar,
Tabs,
Tool Tips,
Menu
"""
import pytest
from ..pages import AccordianPage, AutoCompletePage, DatePickerPage, \
    SliderPage, ProgressBarPage, TabsPage, ToolTipsPage, MenuPage


class TestWidgetsPage:
    """Class represents Widgets tab.
    Accordian,
    Auto Complete,
    Date Picker,
    Slider
    """

    class TestAccordianPage:
        """Class represents Accordian tab tests."""
        accordian_page_link = 'https://demoqa.com/accordian'

        @pytest.mark.parametrize('order', ['first', 'second', 'third'])
        def test_accordian(self, driver, order: str) -> None:
            """Test user can fill the form and sent it."""
            accordian_page = AccordianPage(driver, self.accordian_page_link)
            accordian_page.open()
            title, content = accordian_page.check_accordian(order)
            self.check_title(order, title)
            self.check_content(order, content)

        def check_title(self, accordian_order: str, accordian_title: str) -> None:
            """Check title of accordian."""
            match accordian_order:
                case 'first':
                    expected_title = 'What is Lorem Ipsum?'
                    assert accordian_title == expected_title, \
                        f'Expected first accordian title to be \'{expected_title}\'' \
                        f'Got: {accordian_title}'
                case 'second':
                    expected_title = 'Where does it come from?'
                    assert accordian_title == expected_title, \
                        f'Expected first accordian title to be \'{expected_title}\'' \
                        f'Got: {accordian_title}'
                case 'third':
                    expected_title = 'Why do we use it?'
                    assert accordian_title == expected_title, \
                        f'Expected first accordian title to be \'{expected_title}\'' \
                        f'Got: {accordian_title}'

        def check_content(self, accordian_order: str, accordian_content: str) -> None:
            """Check content of accordian."""
            assert accordian_content is not None, \
                'Expecter to have content of accordian.' \
                f'Got nothing. Accordian number: {accordian_order}'

    class TestAutoCompletePage:
        """Class represents Accordian tab tests."""
        autocomplete_page_link = 'https://demoqa.com/auto-complete'

        def test_fill_multiple_autocomplete(self, driver):
            """Check if multiple autocomplete input is filled."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_page_link)
            autocomplete_page.open()
            colors_selected = autocomplete_page.fill_multiple_input()
            colors_in_multiple_input = autocomplete_page.check_colors_in_multiple_input()
            assert colors_selected == colors_in_multiple_input, \
                'Expected that entered colors match what multiple input shows. \n' \
                f'Entered data: {colors_selected}. \n' \
                f'Shows: {colors_in_multiple_input}'

        def test_remove_color_from_multiple_autocomplete(self, driver):
            """Check if color can be deleted from multiple autocomplete."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_page_link)
            autocomplete_page.open()
            autocomplete_page.fill_multiple_input()
            colors_before_deletion = autocomplete_page.count_colors_in_multiple_input()
            autocomplete_page.remove_single_color_from_multiple_input()
            colors_after_deletion = autocomplete_page.count_colors_in_multiple_input()
            assert colors_before_deletion == colors_after_deletion + 1, \
                f'Expected that {colors_before_deletion} will be greater than ' \
                f'{colors_after_deletion} by 1.\n After deletion single color from multiple input.'

        def test_remove_all_colors_from_multiple_autocomplete(self, driver):
            """Check if all colors can be deleted from multiple autocomplete."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_page_link)
            autocomplete_page.open()
            autocomplete_page.fill_multiple_input()
            colors_before_clearing = autocomplete_page.count_colors_in_multiple_input()
            autocomplete_page.clear_multiple_input()
            colors_after_clearing = autocomplete_page.count_colors_in_multiple_input()
            assert colors_before_clearing > 0, \
                'Expected that some colors was entered in multiple autocomplete input.' \
                f'Got number of entered = {colors_before_clearing}'
            assert colors_after_clearing == 0, \
                f'Expected colors after clearing = 0. ' \
                f'Got: {colors_after_clearing}'

        def test_fill_single_autocomplete(self, driver):
            """Check if single autocomplete input is filled."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_page_link)
            autocomplete_page.open()
            color_selected = autocomplete_page.fill_single_input()
            color_in_single_input = autocomplete_page.check_single_input()
            assert color_selected == color_in_single_input, \
                'Expected that entered color match what single input shows. ' \
                f'Entered data: {color_selected}. Shows: {color_in_single_input}'

    class TestDatePickerPage:
        """Class represents Date Picker tab tests."""
        date_picker_link = 'https://demoqa.com/date-picker'

        def test_select_date(self, driver):
            """Check date can be selected from date select element."""
            date_picker_page = DatePickerPage(driver, self.date_picker_link)
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date_only_from_picker()
            assert date_before != date_after, \
                'Expected date to be different fom than date before. ' \
                f'Got: {date_before=}, {date_after=}'

        def test_select_date_and_time(self, driver):
            """Check date and time can be selected from date and time select element."""
            date_picker_page = DatePickerPage(driver, self.date_picker_link)
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date_and_time()
            assert date_before != date_after, \
                'Expected date to be different fom than date before. ' \
                f'Got: {date_before=}, {date_after=}'

    class TestSliderPage:
        """Class represents Slider tab tests."""
        slider_page_link = 'https://demoqa.com/slider'

        def test_slider(self, driver):
            """Check slider can be moved."""
            slider_page = SliderPage(driver, self.slider_page_link)
            slider_page.open()
            slider_value_before, slider_value_after = slider_page.change_slider_value()
            assert slider_value_before != slider_value_after, \
                'Slider value should change.' \
                f'Got: {slider_value_before=}, {slider_value_after=}.'

    class TestProgressBarPage:
        """Class represents Progress Bar tab tests."""
        progress_bar_page_link = 'https://demoqa.com/progress-bar'

        def test_progress_bar(self, driver):
            """Progress bar changes over time."""
            progress_bar_page = ProgressBarPage(driver, self.progress_bar_page_link)
            progress_bar_page.open()
            progress_bar_before, progress_bar_after = progress_bar_page.change_progress_bar_value()
            assert progress_bar_before != progress_bar_after, \
                'Progress bar value should change.' \
                f'Got: {progress_bar_before=}, {progress_bar_after=}.'

    class TestTabsPage:
        """Class represents Tabs tab tests."""
        tabs_page_link = 'https://demoqa.com/tabs'

        def test_what_tab(self, driver):
            """Tab What has correct name and a content."""
            tabs_page = TabsPage(driver, self.tabs_page_link)
            tabs_page.open()
            actual_tab_name, tab_content_length = tabs_page.check_what_tab()
            expected_tab_name = 'What'
            assert actual_tab_name == expected_tab_name, \
                f'Expected tab name {expected_tab_name}, got {actual_tab_name}.'
            assert tab_content_length > 0, \
                f'Expected that tab has content. Got {tab_content_length=}'

        def test_origin_tab(self, driver):
            """Tab Origin has correct name and a content."""
            tabs_page = TabsPage(driver, self.tabs_page_link)
            tabs_page.open()
            actual_tab_name, tab_content_length = tabs_page.check_origin_tab()
            expected_tab_name = 'Origin'
            assert actual_tab_name == expected_tab_name, \
                f'Expected tab name {expected_tab_name}, got {actual_tab_name}.'
            assert tab_content_length > 0, \
                f'Expected that tab has content. Got {tab_content_length=}'

        def test_use_tab(self, driver):
            """Tab Use has correct name and a content."""
            tabs_page = TabsPage(driver, self.tabs_page_link)
            tabs_page.open()
            actual_tab_name, tab_content_length = tabs_page.check_use_tab()
            expected_tab_name = 'Use'
            assert actual_tab_name == expected_tab_name, \
                f'Expected tab name {expected_tab_name}, got {actual_tab_name}.'
            assert tab_content_length > 0, \
                f'Expected that tab has content. Got {tab_content_length=}'

        def test_more_tab(self, driver):
            """Tab More has correct name and a content."""
            tabs_page = TabsPage(driver, self.tabs_page_link)
            tabs_page.open()
            actual_tab_name, tab_content_length = tabs_page.check_more_tab()
            expected_tab_name = 'More'
            assert actual_tab_name == expected_tab_name, \
                f'Expected tab name {expected_tab_name}, got {actual_tab_name}.'
            assert tab_content_length > 0, \
                f'Expected that tab has content. Got {tab_content_length=}'

    class TestToolTipsPage:
        """Class represents Tool Tips tab tests."""
        tool_tips_page_link = 'https://demoqa.com/tool-tips'

        def test_button_tooltip_text(self, driver):
            """Button has tooltip text."""
            tool_tips_page = ToolTipsPage(driver, self.tool_tips_page_link)
            tool_tips_page.open()
            tooltip_button_text = tool_tips_page.get_tooltip_text_button()
            expected_tooltip_text = 'You hovered over the Button'
            assert tooltip_button_text == expected_tooltip_text, \
                f'Expected tooltip text: {expected_tooltip_text}.' \
                f'Got {tooltip_button_text}.'

        def test_field_tooltip_text(self, driver):
            """Field has tooltip text."""
            tool_tips_page = ToolTipsPage(driver, self.tool_tips_page_link)
            tool_tips_page.open()
            tooltip_field_text = tool_tips_page.get_tooltip_text_field()
            expected_tooltip_text = 'You hovered over the text field'
            assert tooltip_field_text == expected_tooltip_text, \
                f'Expected tooltip text: {expected_tooltip_text}.' \
                f'Got {tooltip_field_text}.'

        def test_contrary_link_tooltip_text(self, driver):
            """Contrary link has tooltip text."""
            tool_tips_page = ToolTipsPage(driver, self.tool_tips_page_link)
            tool_tips_page.open()
            tooltip_contrary_link_text = tool_tips_page.get_tooltip_text_contrary_link()
            expected_tooltip_text = 'You hovered over the Contrary'
            assert tooltip_contrary_link_text == expected_tooltip_text, \
                f'Expected tooltip text: {expected_tooltip_text}.' \
                f'Got {tooltip_contrary_link_text}.'

        def test_section_link_tooltip_text(self, driver):
            """Section link has tooltip text."""
            tool_tips_page = ToolTipsPage(driver, self.tool_tips_page_link)
            tool_tips_page.open()
            tooltip_section_link_text = tool_tips_page.get_tooltip_text_section_link()
            expected_tooltip_text = 'You hovered over the 1.10.32'
            assert tooltip_section_link_text == expected_tooltip_text, \
                f'Expected tooltip text: {expected_tooltip_text}.' \
                f'Got {tooltip_section_link_text}.'

    class TestMenuPage:
        """Class represents Menu tab tests."""
        menu_page_link = 'https://demoqa.com/menu'

        def test_menu_has_main_items(self, driver):
            """Menu has main items."""
            menu_page = MenuPage(driver, self.menu_page_link)
            menu_page.open()
            names_of_items_in_menu = menu_page.get_menu_items_names()
            expected_main_item1 = 'Main Item 1'
            expected_main_item2 = 'Main Item 2'
            expected_main_item3 = 'Main Item 3'
            assert expected_main_item1 in names_of_items_in_menu, \
                f'Expected {expected_main_item1} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
            assert expected_main_item2 in names_of_items_in_menu, \
                f'Expected {expected_main_item2} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
            assert expected_main_item3 in names_of_items_in_menu, \
                f'Expected {expected_main_item3} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'

        def test_menu_has_sub_items(self, driver):
            """Menu has sub items."""
            menu_page = MenuPage(driver, self.menu_page_link)
            menu_page.open()
            names_of_items_in_menu = menu_page.get_menu_items_names()
            expected_sub_item1 = 'Sub Item'
            expected_sub_item2 = 'Sub Item'
            assert expected_sub_item1 in names_of_items_in_menu, \
                f'Expected {expected_sub_item1} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
            assert expected_sub_item2 in names_of_items_in_menu, \
                f'Expected {expected_sub_item2} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'

        def test_menu_has_sub_sub_list(self, driver):
            """Menu has sub sub items."""
            menu_page = MenuPage(driver, self.menu_page_link)
            menu_page.open()
            names_of_items_in_menu = menu_page.get_menu_items_names()
            expected_sub_sub_list = 'SUB SUB LIST »'
            expected_sub_sub_item1 = 'Sub Sub Item 1'
            expected_sub_sub_item2 = 'Sub Sub Item 2'
            assert expected_sub_sub_list in names_of_items_in_menu, \
                f'Expected {expected_sub_sub_list} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
            assert expected_sub_sub_item1 in names_of_items_in_menu, \
                f'Expected {expected_sub_sub_item1} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
            assert expected_sub_sub_item2 in names_of_items_in_menu, \
                f'Expected {expected_sub_sub_item2} in main menu items. ' \
                f'Got {names_of_items_in_menu} without it.'
