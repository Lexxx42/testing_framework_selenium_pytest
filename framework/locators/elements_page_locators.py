from selenium.webdriver.common.by import By


class TextBoxPageLocators():
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


class CheckBoxPageLocators():
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button.rct-option-expand-all')
    ITEM_LIST = (By.CSS_SELECTOR, '.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, '.rct-icon-check')
    TITLE_CHECKBOX = './/ancestor::span[@class=\'rct-text\']'
    OUTPUT_RESULT_LIST = (By.CSS_SELECTOR, '.text-success')


class RadioButtonPageLocators():
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, 'label[for=yesRadio]')
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'label[for=impressiveRadio]')
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, 'label[for=noRadio]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')


class WebTablePageLocators():
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#lastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#userEmail')
    AGE_FIELD = (By.CSS_SELECTOR, '#age')
    SALARY_FIELD = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_FIELD = (By.CSS_SELECTOR, '#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, '.rt-tr-group')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[title=\'Delete\']')
    ROW_PARRENT = './/ancestor::div[@class=\'rt-tr-group\']'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, '.rt-noData')
    SELECT_NUMBER_OF_ROWS = (By.CSS_SELECTOR, '[aria-label=\'rows per page\']')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, '[title=\'Edit\']')
