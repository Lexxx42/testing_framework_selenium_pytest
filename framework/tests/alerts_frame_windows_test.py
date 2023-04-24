from random import randint
from ..pages import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage
from ..generator import generated_person


class TestAlertsFrameWindows:
    EXPECTED_TEXT = 'This is a sample page'

    class TestBrowserWindows:
        browser_windows_link = 'https://demoqa.com/browser-windows'

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_tab_text = browser_windows_page.check_opened('tab')
            assert new_tab_text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'New tab text should be \'This is a sample page\' but got {new_tab_text}'

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_window_text = browser_windows_page.check_opened('window')
            assert new_window_text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'New window text should be \'This is a sample page\' but got {new_window_text}'

    class TestAlerts:
        alerts_page_link = 'https://demoqa.com/alerts'

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            alert_text = alert_page.check_see_alert('alert')
            assert alert_text == 'You clicked a button', \
                f'Alert text should be \'You clicked a button\'. Got {alert_text}'

        def test_see_alert_after_five_sev(self, driver):
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            alert_text = alert_page.check_see_alert('alert_after_five_sec')
            assert alert_text == 'This alert appeared after 5 seconds', \
                f'Alert text should be \'This alert appeared after 5 seconds\'.' \
                f' Got {alert_text}'

        def test_confirm_alert(self, driver):
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
            alert_page = AlertsPage(driver, self.alerts_page_link)
            alert_page.open()
            data_input = next(generated_person()).first_name
            alert_text = alert_page.check_see_alert('prompt', data=data_input)
            assert alert_text == 'Please enter your name', \
                f'Alert text should be \'Please enter your name\'.' \
                f' Got {alert_text}'
            prompt_result = alert_page.check_prompt_result()
            assert prompt_result.split()[-1] == data_input, \
                f'Confirm text should be {data_input}. ' \
                f'Got: {prompt_result.split()[-1]}'

    class TestFrames:
        frames_page_link = 'https://demoqa.com/frames'

        def test_first_frame(self, driver):
            frames_page = FramesPage(driver, self.frames_page_link)
            frames_page.open()
            text, width, height = frames_page.check_frame('frame1')
            assert text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'Frame text should be \'This is a sample page\'.' \
                f' Got {text}'
            assert width == '500px', \
                f'Frame width should be 500px. Got {width}'
            assert height == '350px', \
                f'Frame width should be 350px. Got {height}'

        def test_second_frame(self, driver):
            frames_page = FramesPage(driver, self.frames_page_link)
            frames_page.open()
            text, width, height = frames_page.check_frame('frame2')
            assert text == TestAlertsFrameWindows.EXPECTED_TEXT, \
                f'Frame text should be \'This is a sample page\'.' \
                f' Got {text}'
            assert width == '100px', \
                f'Frame width should be 100px. Got {width}'
            assert height == '100px', \
                f'Frame width should be 100px. Got {height}'

    class TestNestedFrames:
        nested_frames_page_link = 'https://demoqa.com/nestedframes'

        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, self.nested_frames_page_link)
            nested_frames_page.open()
            outer_frame_text, inner_frame_text = nested_frames_page.check_nested_frames()
            assert outer_frame_text == 'Parent frame', \
                f'Parent frame should have a text \'Parent frame\'.' \
                f' Got {outer_frame_text}'
            assert inner_frame_text == 'Child Iframe', \
                f'Child frame should have a text \'Child Iframe\'.' \
                f' Got {inner_frame_text}'

    class TestModalDialogs:
        modal_dialogs_page_link = 'https://demoqa.com/modal-dialogs'

        def test_small_modal_open(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            is_modal_visible = modal_dialog_page.check_modal_visible()
            assert is_modal_visible is True, \
                'Modal dialog should be visible. But it isn\'t.'

        def test_small_modal_close_by_x_button(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_dialog_page.close_modal_by_x_button()
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible. ' \
                'But it is. Closed by x button.'

        def test_small_modal_close_by_close_button(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_dialog_page.close_modal_by_close_button('small')
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible after closing. ' \
                'But it is. Closed by close button.'

        def test_small_modal_text(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_text = modal_dialog_page.get_modal_text('small')
            assert modal_text == 'This is a small modal. It has very less content', \
                'Text in modal dialog don\'t match expected text. ' \
                'Expected: \'This is a small modal. It has very less content\'.' \
                f'Got {modal_text}'

        def test_small_modal_title(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal()
            modal_title = modal_dialog_page.get_modal_title()
            assert modal_title == 'Small Modal', \
                f'Modal title expected: \'Small Modal\'. Got: {modal_title}'

        def test_large_modal_open(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            is_modal_visible = modal_dialog_page.check_modal_visible()
            assert is_modal_visible is True, \
                'Modal dialog should be visible. But it isn\'t.'

        def test_large_modal_close_by_x_button(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_dialog_page.close_modal_by_x_button()
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible. ' \
                'But it is. Closed by x button.'

        def test_large_modal_close_by_close_button(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_dialog_page.close_modal_by_close_button('large')
            is_modal_disappeared = modal_dialog_page.check_modal_disappeared()
            assert is_modal_disappeared is True, \
                'Modal dialog shouldn\'t be visible after closing. ' \
                'But it is. Closed by close button.'

        def test_large_modal_text(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_text = modal_dialog_page.get_modal_text('large')
            assert modal_text == 'Lorem Ipsum is simply dummy text ' \
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
                                 'like Aldus PageMaker including versions of Lorem Ipsum.', \
                'Text in modal dialog don\'t match expected text. ' \
                f'Got {modal_text}'

        def test_small_large_title(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, self.modal_dialogs_page_link)
            modal_dialog_page.open()
            modal_dialog_page.open_modal('large')
            modal_title = modal_dialog_page.get_modal_title()
            assert modal_title == 'Large Modal', \
                f'Modal title expected: \'Large Modal\'. Got: {modal_title}'
