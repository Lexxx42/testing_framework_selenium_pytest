from random import choice
from .base_page import BasePage
from ..locators import BrowserWindowsPageLocators, AlertsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened(self, what_to_open):
        available_cases = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_clickable(available_cases[what_to_open]).click()
        self.switch_to_new_tab()
        text_title = self.element_is_present(self.locators.SAMPLE_TEXT).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self, which_alert='alert', option='Ok', data=None):
        available_alerts = {
            'alert': self.locators.ALERT_BUTTON,
            'alert_after_five_sec': self.locators.ALERT_AFTER_FIVE_SEC_BUTTON,
            'confirm': self.locators.CONFIRM_BUTTON,
            'prompt': self.locators.PROMPT_BUTTON
        }
        self.element_is_clickable(available_alerts[which_alert]).click()
        if which_alert == 'confirm' and option == 'Cancel':
            alert_text = self.switch_to_alert(is_accepted=False)
        elif which_alert == 'prompt':
            alert_text = self.switch_to_alert(is_accepted=True, data=data)
        else:
            alert_text = self.switch_to_alert(is_accepted=True)
        return alert_text

    def check_confirm_result(self):
        confirm_result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return confirm_result

    def check_prompt_result(self):
        prompt_result = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return prompt_result
