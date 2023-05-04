"""Module contains tests for Widgets tab on the site.

Contains tabs:
Accordian,
"""
import pytest
from ..pages import AccordianPage, AutoCompletePage, DatePickerPage


class TestWidgetsPage:
    """Class represents Widgets tab.
    Accordian,
    """

    class TestAccordianPage:
        """Class represents Accordian tab."""
        accordian_link = 'https://demoqa.com/accordian'

        @pytest.mark.parametrize('order', ['first', 'second', 'third'])
        def test_accordian(self, driver, order: str) -> None:
            """Test user can fill the form and sent it."""
            accordian_page = AccordianPage(driver, self.accordian_link)
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
        """Class represents Accordian tab."""
        autocomplete_link = 'https://demoqa.com/auto-complete'

        def test_fill_multiple_autocomplete(self, driver):
            """Check if multiple autocomplete input is filled."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_link)
            autocomplete_page.open()
            colors_selected = autocomplete_page.fill_multiple_input()
            colors_in_multiple_input = autocomplete_page.check_colors_in_multiple_input()
            assert colors_selected == colors_in_multiple_input, \
                'Expected that entered colors match what multiple input shows. \n' \
                f'Entered data: {colors_selected}. \n' \
                f'Shows: {colors_in_multiple_input}'

        def test_remove_color_from_multiple_autocomplete(self, driver):
            """Check if color can be deleted from multiple autocomplete."""
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_link)
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
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_link)
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
            autocomplete_page = AutoCompletePage(driver, self.autocomplete_link)
            autocomplete_page.open()
            color_selected = autocomplete_page.fill_single_input()
            color_in_single_input = autocomplete_page.check_single_input()
            assert color_selected == color_in_single_input, \
                'Expected that entered color match what single input shows. ' \
                f'Entered data: {color_selected}. Shows: {color_in_single_input}'

    class TestDatePickerPage:
        """Class represents Date Picker tab."""
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
