from ..pages import BrowserWindowsPage


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
