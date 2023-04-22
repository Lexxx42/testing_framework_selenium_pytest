from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, '#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, '#windowButton')

    # new tab and window text
    SAMPLE_TEXT = (By.CSS_SELECTOR, '#sampleHeading')


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, '#alertButton')
    ALERT_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, '#timerAlertButton')

    CONFIRM_BUTTON = (By.CSS_SELECTOR, '#confirmButton')
    CONFIRM_RESULT = (By.CSS_SELECTOR, '#confirmResult')

    PROMPT_BUTTON = (By.CSS_SELECTOR, '#promtButton')
