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
    PROMPT_RESULT = (By.CSS_SELECTOR, '#promptResult')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, '#frame1')
    SECOND_FRAME = (By.CSS_SELECTOR, '#frame2')
    FRAME_TEXT = (By.CSS_SELECTOR, '#sampleHeading')


class NestedFramesPageLocators:
    OUTER_FRAME = (By.CSS_SELECTOR, '#frame1')
    OUTER_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    INNER_FRAME = (By.CSS_SELECTOR, '[srcdoc=\'<p>Child Iframe</p>\']')
    INNER_FRAME_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    MODAL_WINDOW = (By.CSS_SELECTOR, '.modal-content')
    MODAL_CLOSE_X_BUTTON = (By.CSS_SELECTOR, '.close')
    MODAL_TITLE = (By.CSS_SELECTOR, '.modal-title.h4')

    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, '#showSmallModal')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '#closeSmallModal')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, '.modal-body')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, '#showLargeModal')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '#closeLargeModal')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, '.modal-content p')
