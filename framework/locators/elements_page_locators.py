"""This module contains locators for Elements tab on the site.

Contains locators for following tabs:
Browser Windows,
Alerts,
Frames,
Nested Frames,
Modal Dialogs.
"""
from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Class for Text Box page locators."""
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


class CheckBoxPageLocators:
    """Class for Check Box page locators."""
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button.rct-option-expand-all')
    ITEM_LIST = (By.CSS_SELECTOR, '.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, '.rct-icon-check')
    TITLE_CHECKBOX = './/ancestor::span[@class=\'rct-text\']'
    OUTPUT_RESULT_LIST = (By.CSS_SELECTOR, '.text-success')


class RadioButtonPageLocators:
    """Class for Radio Button page locators."""
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, 'label[for=yesRadio]')
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'label[for=impressiveRadio]')
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, 'label[for=noRadio]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')


class WebTablePageLocators:
    """Class for Web Tables page locators."""
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
    ROW_PARENT = './/ancestor::div[@class=\'rt-tr-group\']'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, '.rt-noData')
    SELECT_NUMBER_OF_ROWS = (By.CSS_SELECTOR, '[aria-label=\'rows per page\']')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, '[title=\'Edit\']')


class ButtonsPageLocators:
    """Class for Buttons page locators."""
    # buttons
    DOUBLE_CLICK_ME_BUTTON = (By.CSS_SELECTOR, '#doubleClickBtn')
    RIGHT_CLICK_ME_BUTTON = (By.CSS_SELECTOR, '#rightClickBtn')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    # messages
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, '#doubleClickMessage')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, '#rightClickMessage')
    CLICK_MESSAGE = (By.CSS_SELECTOR, '#dynamicClickMessage')


class LinksPageLocators:
    """Class for Links page locators."""
    # new tab links
    SIMPLE_LINK = (By.CSS_SELECTOR, '#simpleLink')
    DYNAMIC_LINK = (By.CSS_SELECTOR, '#dynamicLink')

    # api calls
    BAD_REQUEST = (By.CSS_SELECTOR, '#bad-request')
    CREATED_REQUEST = (By.CSS_SELECTOR, '#created')
    NO_CONTENT_REQUEST = (By.CSS_SELECTOR, '#no-content')
    MOVED_REQUEST = (By.CSS_SELECTOR, '#moved')
    UNAUTHORIZED_REQUEST = (By.CSS_SELECTOR, '#unauthorized')
    FORBIDDEN_REQUEST = (By.CSS_SELECTOR, '#forbidden')
    NOT_FOUND_REQUEST = (By.CSS_SELECTOR, '#invalid-url')


class BrokenLinksPageLocators:
    """Class for Broken Links page locators."""
    VALID_IMAGE = (By.CSS_SELECTOR, '.col-md-6>div:nth-child(2) img:nth-child(2)')
    BROKEN_IMAGE = (By.XPATH, '//div[2]/div[2]/img[2]')
    VALID_LINK = (By.XPATH, '//div[2]/div[2]/a[1]')
    BROKEN_LINK = (By.XPATH, '//div[2]/div[2]/a[2]')


class UploadAndDownloadPageLocators:
    """Class for Upload and Download page locators."""
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, '#uploadFile')
    UPLOADED_RESULT = (By.CSS_SELECTOR, '#uploadedFilePath')
    DOWNLOAD_FILE_BUTTON = (By.CSS_SELECTOR, '#downloadButton')


class DynamicPropertiesPageLocators:
    """Class for Dynamic Properties page locators."""
    ENABLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, '#enableAfter')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, '#colorChange')
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, '#visibleAfter')
