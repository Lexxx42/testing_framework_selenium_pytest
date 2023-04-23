from random import randint
from ..pages import BrowserWindowsPage, AlertsPage
from ..generator import generated_person


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        browser_windows_link = 'https://demoqa.com/browser-windows'

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_tab_text = browser_windows_page.check_opened('tab')
            assert new_tab_text == 'This is a sample page', \
                f'New tab text should be \'This is a sample page\' but got {new_tab_text}'

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.browser_windows_link)
            browser_windows_page.open()
            new_window_text = browser_windows_page.check_opened('window')
            assert new_window_text == 'This is a sample page', \
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
