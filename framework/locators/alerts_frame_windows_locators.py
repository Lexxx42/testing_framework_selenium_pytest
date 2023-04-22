from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, '#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, '#windowButton')

    # new tab and window text
    SAMPLE_TEXT = (By.CSS_SELECTOR, '#sampleHeading')
