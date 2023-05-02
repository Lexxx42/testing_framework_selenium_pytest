"""This module contains page objects for Alerts, Frame & Windows tab on the site.

Contains page objects for:
Browser Windows,
Alerts,
Frames,
Nested Frames,
Modal Dialogs.
"""
from .base_page import BasePage
from ..locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators


class BrowserWindowsPage(BasePage):
    """Browser Windows page object."""
    locators = BrowserWindowsPageLocators()

    def check_opened(self, what_to_open) -> str:
        """
        Check if new tab of window is opened.
        :returns: title of new tab or window.
        """
        available_cases = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_clickable(available_cases[what_to_open]).click()
        self.switch_to_new_tab()
        text_title = self.element_is_present(self.locators.SAMPLE_TEXT).text
        return text_title


class AlertsPage(BasePage):
    """Alerts page object."""
    locators = AlertsPageLocators()

    def check_see_alert(self, which_alert='alert', option='Ok', data=None) -> str:
        """
        Check if alert, confirm or prompt is has a text.
        :param which_alert: type of alert ['alert', 'alert_after_five_sec', 'confirm', 'prompt'].
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
        self.element_is_clickable(available_alerts[which_alert]).click()
        if which_alert == 'confirm' and option == 'Cancel':
            alert_text = self.get_alert_text(is_accepted=False)
        elif which_alert == 'prompt':
            alert_text = self.get_alert_text(is_accepted=True, data=data)
        else:
            alert_text = self.get_alert_text(is_accepted=True)
        return alert_text

    def check_confirm_result(self) -> str:
        """
        Check confirm result text.
        :returns: confirmation confirm result text.
        """
        confirm_result = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return confirm_result

    def check_prompt_result(self) -> str:
        """
        Check prompt result text.
        :returns: confirmation prompt result text.
        """
        prompt_result = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return prompt_result


class FramesPage(BasePage):
    """Frames page object."""
    locators = FramesPageLocators()

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
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
        except AttributeError:
            width = -1
            height = -1
        self.switch_to_frame(frame)
        text = self.element_is_present(self.locators.FRAME_TEXT).text
        return text, width, height


class NestedFramesPage(BasePage):
    """Nested Frames page object."""
    locators = NestedFramesPageLocators()

    def check_nested_frames(self) -> tuple[str, str]:
        """
        Check if parent frame has a child one. Returns text in frames.
        :returns: text of parent and child frame.
        """
        parent_frame = self.element_is_visible(self.locators.OUTER_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.OUTER_FRAME_TEXT).text
        child_frame = self.element_is_visible(self.locators.INNER_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.INNER_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    """Modal Dialogs page object."""
    locators = ModalDialogsPageLocators()

    def open_modal(self, which_modal='small') -> None:
        """Opens modal."""
        if which_modal == 'small':
            self.element_is_clickable(self.locators.SMALL_MODAL_BUTTON).click()
        elif which_modal == 'large':
            self.element_is_clickable(self.locators.LARGE_MODAL_BUTTON).click()

    def check_modal_visible(self) -> bool:
        """
        Checks if modal is visible.
        :returns: True if modal is visible.
        """
        return self.is_element_visible(self.locators.MODAL_WINDOW)

    def check_modal_disappeared(self) -> bool:
        """
        Checks if modal is disappeared.
        :returns: True if modal is disappeared.
        """
        return self.is_element_disappeared(self.locators.MODAL_WINDOW)

    def close_modal_by_x_button(self) -> None:
        """Close modal by X button."""
        self.element_is_clickable(self.locators.MODAL_CLOSE_X_BUTTON).click()

    def close_modal_by_close_button(self, which_modal='small') -> None:
        """Close modal by Close button."""
        if which_modal == 'small':
            self.element_is_clickable(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        elif which_modal == 'large':
            self.element_is_clickable(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()

    def get_modal_text(self, which_modal='small') -> str:
        """
        Returns text from modal.
        :param which_modal: type of modal window ['small', 'large']
        :returns: text from modal.
        """
        if which_modal == 'small':
            return self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        if which_modal == 'large':
            return self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text

    def get_modal_title(self) -> str:
        """Returns title from modal."""
        return self.element_is_visible(self.locators.MODAL_TITLE).text
