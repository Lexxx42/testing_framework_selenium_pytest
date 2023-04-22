from .base_page import BasePage
from ..locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators

    def check_opened(self, what_to_open):
        available_cases = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_clickable(available_cases[what_to_open]).click()
        self.switch_to_new_tab()
        text_title = self.element_is_present(self.locators.SAMPLE_TEXT).text
        return text_title
