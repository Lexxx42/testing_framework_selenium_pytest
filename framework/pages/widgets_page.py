"""Module contains tests for Widgets tab on the site.

Contains page objects for:
Accordian,
Auto Complete,
Date Picker,
Slider,
Progress Bar,
Tabs,
Tool Tips,
Menu.
"""
from random import sample, randint, choice
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from ..generator import generated_color, generated_date
from ..locators import AccordianPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators, \
    TabsPageLocators, ToolTipsPageLocators, MenuPageLocators


class AccordianPage(BasePage):
    """Accordian page object."""
    locators = AccordianPageLocators()

    @allure.step('Receive accordian order.')
    def check_accordian(self, accordian_order: str) -> tuple[str, str]:
        """
        Receive accordian order: 'first', 'second', 'third'.
        \nReturns section title, section content.
        :returns: Text of section title and section content.
        """
        accordian = {
            'first': {
                'title': self.locators.FIRST_SECTION,
                'content': self.locators.FIRST_SECTION_TEXT
            },
            'second': {
                'title': self.locators.SECOND_SECTION,
                'content': self.locators.SECOND_SECTION_TEXT
            },
            'third': {
                'title': self.locators.THIRD_SECTION,
                'content': self.locators.THIRD_SECTION_TEXT
            }
        }
        with allure.step('Click on section title'):
            section_title = self.element_is_clickable(accordian[accordian_order]['title'])
            section_title.click()
        try:
            with allure.step('Get section content'):
                section_content = \
                    self.element_is_visible(accordian[accordian_order]['content']).text
        except TimeoutException as error:
            with allure.step(f'Get section content with {error}'):
                section_title.click()
                section_content = \
                    self.element_is_visible(accordian[accordian_order]['content']).text
        return section_title.text, section_content


class AutoCompletePage(BasePage):
    """Auto Complete page object."""
    locators = AutoCompletePageLocators()

    @allure.step('Fill multiple input with random from 2 to 5 available colors.')
    def fill_multiple_input(self) -> list[str]:
        """
        Fill multiple input with random from 2 to 5 available colors.
        :returns: Colors generated object.
        """
        with allure.step('Get two generated colors'):
            colors = sample(next(generated_color()).color_name, k=randint(2, 5))
        for color in colors:
            with allure.step(f'Check {color=} in input'):
                multiple_input = self.element_is_clickable(self.locators.MULTIPLE_INPUT)
                multiple_input.send_keys(color)
                multiple_input.send_keys(Keys.ENTER)
        return colors

    @allure.step('Removes 1 color from selected colors in multiple input.')
    def remove_single_color_from_multiple_input(self) -> None:
        """
        Removes 1 color from selected colors in multiple input.
        """
        remove_buttons = self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEM_DELETE)
        for remove_button in remove_buttons:
            with allure.step('Click on remove button'):
                remove_button.click()
            break

    @allure.step('Get the number of colors in input.')
    def get_number_of_colors_in_multiple_input(self) -> int:
        """
        Get the number of colors in input.
        :returns: Quantity of colors in multiple input.
        """
        try:
            return len(self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS))
        except TimeoutException:
            return 0

    @allure.step('')
    def clear_multiple_input(self) -> None:
        """
        Removes all colors from multiple input.
        """
        clear_button = self.element_is_clickable(self.locators.MULTIPLE_INPUT_CLEAR_BUTTON)
        clear_button.click()

    def check_colors_in_multiple_input(self) -> list[str]:
        """
        Checks colors in multiple input.
        :returns: Colors present in multiple input.
        """
        colors = self.elements_are_present(self.locators.MULTIPLE_INPUT_ITEMS)
        colors_in_multiple_input = []
        for color in colors:
            colors_in_multiple_input.append(color.text)
        return colors_in_multiple_input

    def fill_single_input(self) -> str:
        """
        Fill single input with random color.
        :returns: Color entered in input.
        """
        color = sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_single_input(self) -> str:
        """
        Check color in single input.
        :return: Color present in single input.
        """
        color_in_single_input = self.element_is_visible(self.locators.SINGLE_INPUT_ITEM)
        return color_in_single_input.text


class DatePickerPage(BasePage):
    """Date Picker page object."""
    locators = DatePickerPageLocators()

    def select_date_only_from_picker(self) -> tuple[str, str]:
        """
        Select date from picker
        :returns: date before and after selection from date picker.
        """
        date = next(generated_date())
        input_date = self.element_is_clickable(self.locators.DATE_INPUT)
        value_date_before_selection = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_MONTH_SELECT, date.month)
        self.select_date_by_text(self.locators.DATE_YEAR_SELECT, date.year)
        self.select_element_from_elements_by_text(self.locators.DATE_AVAILABLE_DAYS, date.day)
        value_date_after_selection = input_date.get_attribute('value')
        return value_date_before_selection, value_date_after_selection

    def select_date_and_time(self) -> tuple[str, str]:
        """
        Select date and time from picker
        :returns: date before and after selection from date and time picker.
        """
        date = next(generated_date())
        input_date = self.element_is_clickable(self.locators.DATE_AND_TIME_INPUT)
        value_date_before_selection = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH_VIEW).click()
        self.select_element_from_elements_by_text(
            self.locators.DATE_AND_TIME_AVAILABLE_MONTHS, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR_VIEW).click()
        available_years = self.elements_are_visible(
            self.locators.DATE_AND_TIME_AVAILABLE_YEARS)
        choice(available_years).click()
        self.select_element_from_elements_by_text(self.locators.DATE_AVAILABLE_DAYS, date.day)
        self.select_element_from_elements_by_text(
            self.locators.DATE_AND_TIME_AVAILABLE_TIMES, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after_selection = input_date_after.get_attribute('value')
        return value_date_before_selection, value_date_after_selection


class SliderPage(BasePage):
    """Slider page object."""
    locators = SliderPageLocators()

    def change_slider_value(self):
        """
        Changes slider value.
        :returns: Value before and after change.
        """
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.drag_and_drop_by_offset(slider_input, randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        if value_after == 25:  # Default slider value.
            self.drag_and_drop_by_offset(slider_input, 26, 0)
            value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    """Progress Bar page object."""
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        """
        Changes the progress bar value.
        :returns: Value before and after change.
        """
        import time
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        start_stop_button = self.element_is_clickable(self.locators.START_STOP_BUTTON)
        start_stop_button.click()
        time.sleep(randint(2, 4))
        start_stop_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    """Progress Bar page object."""
    locators = TabsPageLocators()

    def check_what_tab(self) -> tuple[str, int]:
        """
        Checks content of what tab.
        :returns: Tab name, content of the tab length.
        """
        what_tab_button = self.element_is_clickable(self.locators.TAB_WHAT)
        what_tab_button.click()
        tab_name = what_tab_button.text
        what_tab_content = self.element_is_visible(self.locators.TAB_WHAT_CONTENT).text
        return tab_name, len(what_tab_content)

    def check_origin_tab(self) -> tuple[str, int]:
        """
        Checks content of origin tab.
        :returns: Tab name, content of the tab length.
        """
        origin_tab_button = self.element_is_clickable(self.locators.TAB_ORIGIN)
        origin_tab_button.click()
        tab_name = origin_tab_button.text
        origin_tab_content = self.element_is_visible(self.locators.TAB_ORIGIN_CONTENT).text
        return tab_name, len(origin_tab_content)

    def check_use_tab(self) -> tuple[str, int]:
        """
        Checks content of use tab.
        :returns: Tab name, content of the tab length.
        """
        use_tab_button = self.element_is_clickable(self.locators.TAB_USE)
        use_tab_button.click()
        tab_name = use_tab_button.text
        use_tab_content = self.element_is_visible(self.locators.TAB_USE_CONTENT).text
        return tab_name, len(use_tab_content)

    def check_more_tab(self) -> tuple[str, int]:
        """
        Checks content of more tab.
        :returns: Tab name, content of the tab length.
        """
        more_tab_button = self.element_is_clickable(self.locators.TAB_MORE)
        more_tab_button.click()
        tab_name = more_tab_button.text
        more_tab_content = self.element_is_visible(self.locators.TAB_MORE_CONTENT).text
        return tab_name, len(more_tab_content)


class ToolTipsPage(BasePage):
    """Progress Bar page object."""
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tip(self, hovered_element, hover_tip_element) -> str:
        # TODO: Make change of color of the button like this.
        """
        Get the tooltip text from the element.
        :param hovered_element: The element to get the tooltip text from.
        :param hover_tip_element: The element with the tooltip.
        :returns: The tooltip text.
        """
        element = self.element_is_visible(hovered_element)
        self.move_cursor_to_center_of_element(element)
        self.element_is_visible(hover_tip_element)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS_INNERS).text
        return tooltip_text

    def get_tooltip_text_button(self) -> str:
        """
        Check if the button tooltip is visible.
        :returns: Tooltip text.
        """
        tooltip_text_button = self.get_text_from_tool_tip(self.locators.BUTTON, self.locators.TOOLTIP_BUTTON)
        return tooltip_text_button

    def get_tooltip_text_field(self) -> str:
        """
        Check if the field tooltip is visible.
        :returns: Tooltip text.
        """
        tooltip_text_field = self.get_text_from_tool_tip(self.locators.FIELD, self.locators.TOOLTIP_FIELD)
        return tooltip_text_field

    def get_tooltip_text_contrary_link(self) -> str:
        """
        Check if the contrary link tooltip is visible.
        :returns: Tooltip text.
        """
        tooltip_text_contrary_link = self.get_text_from_tool_tip(self.locators.CONTRARY_LINK,
                                                                 self.locators.TOOLTIP_CONTRARY_LINK)
        return tooltip_text_contrary_link

    def get_tooltip_text_section_link(self) -> str:
        """
        Check if the section link tooltip is visible.
        :returns: Tooltip text.
        """
        tooltip_text_section_link = self.get_text_from_tool_tip(self.locators.SECTION_LINK,
                                                                self.locators.TOOLTIP_SECTION_LINK)
        return tooltip_text_section_link


class MenuPage(BasePage):
    """Menu page object."""
    locators = MenuPageLocators()

    def get_menu_items_names(self) -> list[str]:
        """
        Get the names of the items in the menu.
        :returns: Names of the items in the menu.
        """
        menu_items = self.elements_are_present(self.locators.MENU_ITEMS)
        items_names = []
        for item in menu_items:
            self.move_cursor_to_center_of_element(item)
            items_names.append(item.text)
        return items_names
