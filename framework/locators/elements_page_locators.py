from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '.form-control#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '.form-control#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p#currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p#permanentAddress')
