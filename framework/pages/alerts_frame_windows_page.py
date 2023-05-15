"""This module contains page objects for Alerts, Frame & Windows tab on the site.

Contains page objects for:
Browser Windows,
Alerts,
Frames,
Nested Frames,
Modal Dialogs.
"""
import allure
from .base_page import BasePage
from ..locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators


class BrowserWindowsPage(BasePage):
    """Browser Windows page object."""
    locators = BrowserWindowsPageLocators()

    @allure.step('Check if new tab of window is opened.')
    def check_opened(self, what_to_open) -> str:
        """
        Check if new tab of window is opened.
        :returns: title of new tab or window.
        """
        available_cases = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        with allure.step(f'Click on {what_to_open}'):
            self.element_is_clickable(available_cases[what_to_open]).click()
        with allure.step('Switch to new tab'):
            self.switch_to_new_tab()
        with allure.step('Get title text'):
            text_title = self.element_is_present(self.locators.SAMPLE_TEXT).text
        return text_title


class AlertsPage(BasePage):
    """Alerts page object."""
    locators = AlertsPageLocators()

    @allure.step('Check if alert, confirm or prompt is has a text.')
    def check_see_alert(self, alert_type='alert', option='Ok', data=None) -> str:
        """
        Check if alert, confirm or prompt is has a text.
        :param alert_type: type of alert ['alert', 'alert_after_five_sec', 'confirm', 'prompt'].
        :param option: confirm alert or not ['Ok', 'Cancel'].
        :param data: data to be sent to the alert.
        :returns: text of alert message.
        """
        available_alerts = {
            'alert': self.locators.ALERT_BUTTON,
            'alert_after_five_sec': self.locators.ALERT_AFTER_FIVE_SEC_BUTTON,
            'confirm': self.locators.CONFIRM_BUTTON,
            'prompt': self.locators.PROMPT_BUTTON
        }
        with allure.step(f'Click on {alert_type=}'):
            self.element_is_clickable(available_alerts[alert_type]).click()
        with allure.step('Get alert text'):
            if alert_type == 'confirm' and option == 'Cancel':
                alert_text = self.get_alert_text(is_accepted=False)
            elif alert_type == 'prompt':
                alert_text = self.get_alert_text(is_accepted=True, data=data)
            else:
                alert_text = self.get_alert_text(is_accepted=True)
        return alert_text

    @allure.step('Get confirm result text.')
    def get_confirm_result(self) -> str:
        """
        Get confirm result text.
        :returns: confirmation confirm result text.
        """
        confirm_result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return confirm_result

    @allure.step('Get prompt result text.')
    def get_prompt_result(self) -> str:
        """
        Get prompt result text.
        :returns: confirmation prompt result text.
        """
        prompt_result = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return prompt_result


class FramesPage(BasePage):
    """Frames page object."""
    locators = FramesPageLocators()

    @allure.step('Check width, height and a text of opened frame.')
    def check_frame(self, frame_number) -> tuple[str, int, int]:
        """
        Check width, height and a text of opened frame.
        :returns: text of opened frame, it's width and height.
        """
        frame = None
        if frame_number == 'frame1':
            frame = self.element_is_visible(self.locators.FIRST_FRAME)
        elif frame_number == 'frame2':
            frame = self.element_is_visible(self.locators.SECOND_FRAME)
        try:
            with allure.step('Get width and height of opened frame'):
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
        except AttributeError:
            width = -1
            height = -1
        with allure.step('Switch to new tab'):
            self.switch_to_frame(frame)
        with allure.step('Get text from frame'):
            text = self.element_is_present(self.locators.FRAME_TEXT).text
        return text, width, height


class NestedFramesPage(BasePage):
    """Nested Frames page object."""
    locators = NestedFramesPageLocators()

    @allure.step('Check if parent frame has a child one. Returns text in frames.')
    def check_nested_frames(self) -> tuple[str, str]:
        """
        Check if parent frame has a child one. Returns text in frames.
        :returns: text of parent and child frame.
        """
        parent_frame = self.element_is_visible(self.locators.OUTER_FRAME)
        with allure.step('Switch to parent frame'):
            self.switch_to_frame(parent_frame)
        with allure.step('Get parent frame text'):
            parent_text = self.element_is_present(self.locators.OUTER_FRAME_TEXT).text
        child_frame = self.element_is_visible(self.locators.INNER_FRAME)
        with allure.step('Switch to child frame'):
            self.switch_to_frame(child_frame)
        with allure.step('Get child frame text'):
            child_text = self.element_is_present(self.locators.INNER_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    """Modal Dialogs page object."""
    locators = ModalDialogsPageLocators()

    @allure.step('Opens modal.')
    def open_modal(self, which_modal='small') -> None:
        """Opens modal."""
        if which_modal == 'small':
            self.element_is_clickable(self.locators.SMALL_MODAL_BUTTON).click()
        elif which_modal == 'large':
            self.element_is_clickable(self.locators.LARGE_MODAL_BUTTON).click()

    @allure.step('Checks if modal is visible.')
    def check_modal_visible(self) -> bool:
        """
        Checks if modal is visible.
        :returns: True if modal is visible.
        """
        return self.is_element_visible(self.locators.MODAL_WINDOW)

    @allure.step('Checks if modal is disappeared.')
    def check_modal_disappeared(self) -> bool:
        """
        Checks if modal is disappeared.
        :returns: True if modal is disappeared.
        """
        return self.is_element_disappeared(self.locators.MODAL_WINDOW)

    @allure.step('Close modal by X button.')
    def close_modal_by_x_button(self) -> None:
        """Close modal by X button."""
        self.element_is_clickable(self.locators.MODAL_CLOSE_X_BUTTON).click()

    @allure.step('Close modal by Close button.')
    def close_modal_by_close_button(self, which_modal='small') -> None:
        """Close modal by Close button."""
        if which_modal == 'small':
            self.element_is_clickable(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        elif which_modal == 'large':
            self.element_is_clickable(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()

    @allure.step('Returns text from modal.')
    def get_modal_text(self, which_modal='small') -> str:
        """
        Returns text from modal.
        :param which_modal: type of modal window ['small', 'large'].
        :returns: text from modal.
        """
        text_locator = None
        if which_modal == 'small':
            text_locator = self.locators.SMALL_MODAL_TEXT
        if which_modal == 'large':
            text_locator = self.locators.LARGE_MODAL_TEXT
        return self.element_is_visible(text_locator).text

    @allure.step('Returns title from modal.')
    def get_modal_title(self) -> str:
        """Returns title from modal."""
        return self.element_is_visible(self.locators.MODAL_TITLE).text
