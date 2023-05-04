"""Module contains tests for Alerts, Frame & Windows tab on the site.

Contains tabs:
Browser Windows,
Alerts,
Frames,
Nested Frames,
Modal Dialogs.
"""
from random import randint
from ..pages import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage
from ..generator import generated_person


class TestAlertsFrameWindows:
    """Class represents Alerts, Frame & Windows tab.
    Contains tabs:
    Browser Windows,
    Alerts,
    Frames,
    Nested Frames,
    Modal Dialogs.
    """
    EXPECTED_TEXT = 'This is a sample page'

    class TestBrowserWindows:
        """Class represents Browser Windows tab."""
        browser_windows_link = 'https://demoqa.com/browser-windows'

        def test_new_tab(self, driver):
            """Test opening a new tab and getting the text from it."""
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_tab_text = browser_windows_page.check_opened('tab')
            assert new_tab_text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'New tab text should be \'This is a sample page\' but got {new_tab_text}'

        def test_new_window(self, driver):
            """Test opening a new window and getting the text from it."""
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_window_text = browser_windows_page.check_opened('window')
            assert new_window_text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'New window text should be \'This is a sample page\' but got {new_window_text}'

    class TestAlerts:
        """Class represents Alerts tab."""
        alerts_page_link = 'https://demoqa.com/alerts'

        def test_see_alert(self, driver):
            """Test user can see alert and the text of it."""
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            alert_text = alert_page.check_see_alert('alert')
            assert alert_text == 'You clicked a button', \
                f'Alert text should be \'You clicked a button\'. Got {alert_text}'

        def test_see_alert_after_five_sev(self, driver):
            """Test alert is opened after 5 seconds after a click."""
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            alert_text = alert_page.check_see_alert('alert_after_five_sec')
            assert alert_text == 'This alert appeared after 5 seconds', \
                f'Alert text should be \'This alert appeared after 5 seconds\'.' \
                f' Got {alert_text}'

        def test_confirm_alert(self, driver):
            """Test user can interact with a confirm alert."""
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            options = ['Ok', 'Cancel']
            selected_option = options[randint(-1, 0)]
            alert_text = alert_page.check_see_alert('confirm', option=selected_option)
            assert alert_text == 'Do you confirm action?', \
                f'Alert text should be \'Do you confirm action?\'.' \
                f' Got {alert_text}'
            confirm_result = alert_page.check_confirm_result()
            assert confirm_result == f'You selected {selected_option}', \
                f'Confirm text should be \'You selected (Ok or Cancel)\'. ' \
                f'Got: You selected {selected_option}'

        def test_prompt_alert(self, driver):
            """Test user can interact with a prompt alert."""
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            data_input = next(generated_person()).first_name
            alert_text = alert_page.check_see_alert('prompt', data=data_input)
            expected_alert_text = 'Please enter your name'
            assert alert_text == expected_alert_text, \
                f'Alert text should be \'{expected_alert_text}\'.' \
                f' Got {alert_text}'
            prompt_result = alert_page.check_prompt_result()
            assert prompt_result.split()[-1] == data_input, \
                f'Confirm text should be {data_input}. ' \
                f'Got: {prompt_result.split()[-1]}'

    class TestFrames:
        """Class represents Frames tab."""
        frames_page_link = 'https://demoqa.com/frames'

        def test_first_frame(self, driver):
            """Test user can see text in a frame. Frame has correct resolution."""
            frames_page = FramesPage(driver, self.frames_page_link)
            frames_page.open()
            text, width, height = frames_page.check_frame('frame1')
            expected_width = '500px'
            expected_height = '350px'
            assert text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'Frame text should be \'This is a sample page\'.' \
                f' Got {text}'
            assert width == expected_width, \
                f'Frame width should be {expected_width}. Got {width}'
            assert height == expected_height, \
                f'Frame width should be {expected_height}. Got {height}'

        def test_second_frame(self, driver):
            """Test user can see text in a frame. Frame has correct resolution."""
            frames_page = FramesPage(driver, self.frames_page_link)
            frames_page.open()
            text, width, height = frames_page.check_frame('frame2')
            expected_width = '100px'
            expected_height = '100px'
            assert text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'Frame text should be \'This is a sample page\'.' \
                f' Got {text}'
            assert width == expected_width, \
                f'Frame width should be {expected_width}. Got {width}'
            assert height == expected_height, \
                f'Frame width should be {expected_height}. Got {height}'

    class TestNestedFrames:
        """Class represents Nested Frames tab."""
        nested_frames_page_link = 'https://demoqa.com/nestedframes'

        def test_nested_frames(self, driver):
            """Test user can see text in a parent and child frames."""
            nested_frames_page = NestedFramesPage(driver, self.nested_frames_page_link)
            nested_frames_page.open()
            outer_frame_text, inner_frame_text = nested_frames_page.check_nested_frames()
            expected_parent_text = 'Parent frame'
            expected_child_text = 'Child Iframe'
            assert outer_frame_text == expected_parent_text, \
                f'Parent frame should have a text \'{expected_parent_text}\'.' \
                f' Got {outer_frame_text}'
            assert inner_frame_text == expected_child_text, \
                f'Child frame should have a text \'{expected_child_text}\'.' \
                f' Got {inner_frame_text}'

    class TestModalDialogs:
        """Class represents Modal Dialogs tab."""
        modal_dialogs_page_link = 'https://demoqa.com/modal-dialogs'

        def test_small_modal_open(self, driver):
            """Test user can open small modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            is_modal_visible = modal_dialog_page.check_modal_visible()
            assert is_modal_visible is True, \
                'Modal dialog should be visible. But it isn\'t.'

        def test_small_modal_close_by_x_button(self, driver):
            """Test user can close small modal by X button."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_dialog_page.close_modal_by_x_button()
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible. ' \
                'But it is. Closed by x button.'

        def test_small_modal_close_by_close_button(self, driver):
            """Test user can close small modal by Close button."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_dialog_page.close_modal_by_close_button('small')
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible after closing. ' \
                'But it is. Closed by close button.'

        def test_small_modal_text(self, driver):
            """Test user can read text in a small modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_text = modal_dialog_page.get_modal_text('small')
            expected_modal_text = 'This is a small modal. It has very less content'
            assert modal_text == expected_modal_text, \
                'Text in modal dialog don\'t match expected text. ' \
                f'Expected: \'{expected_modal_text}\'.' \
                f'Got {modal_text}'

        def test_small_modal_title(self, driver):
            """Test user can read title of a small modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_title = modal_dialog_page.get_modal_title()
            expected_title = 'Small Modal'
            assert modal_title == expected_title, \
                f'Modal title expected: \'{expected_title}\'. Got: {modal_title}'

        def test_large_modal_open(self, driver):
            """Test user can open large modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            is_modal_visible = modal_dialog_page.check_modal_visible()
            assert is_modal_visible is True, \
                'Modal dialog should be visible. But it isn\'t.'

        def test_large_modal_close_by_x_button(self, driver):
            """Test user can close large modal by X button."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_dialog_page.close_modal_by_x_button()
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible. ' \
                'But it is. Closed by x button.'

        def test_large_modal_close_by_close_button(self, driver):
            """Test user can close large modal by Close button."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_dialog_page.close_modal_by_close_button('large')
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible after closing. ' \
                'But it is. Closed by close button.'

        def test_large_modal_text(self, driver):
            """Test user can read text in a large modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_text = modal_dialog_page.get_modal_text('large')
            expected_modal_text = 'Lorem Ipsum is simply dummy text ' \
                                  'of the printing and typesetting industry.' \
                                  ' Lorem Ipsum has been the industry\'s standard' \
                                  ' dummy text ever since the 1500s, when an unknown' \
                                  ' printer took a galley of type and scrambled' \
                                  ' it to make a type specimen book. ' \
                                  'It has survived not only five centuries, ' \
                                  'but also the leap into electronic typesetting, ' \
                                  'remaining essentially unchanged. ' \
                                  'It was popularised in the 1960s with the release of ' \
                                  'Letraset sheets containing Lorem Ipsum passages, ' \
                                  'and more recently with desktop publishing software ' \
                                  'like Aldus PageMaker including versions of Lorem Ipsum.'
            assert modal_text == expected_modal_text, \
                'Text in modal dialog don\'t match expected text. ' \
                f'Got {modal_text}'

        def test_large_modal_title(self, driver):
            """Test user can read title of a large modal."""
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_title = modal_dialog_page.get_modal_title()
            expected_title = 'Large Modal'
            assert modal_title == expected_title, \
                f'Modal title expected: \'{expected_title}\'. Got: {modal_title}'
