"""This module contains locators for Widgets tab on the site.

Contains locators for following tabs:
Accordian,
"""
from selenium.webdriver.common.by import By


class AccordianPageLocators:
    """Class for Accordian page locators."""
    FIRST_SECTION = (By.CSS_SELECTOR, '#section1Heading')
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, '#section1Content p')

    SECOND_SECTION = (By.CSS_SELECTOR, '#section2Heading')
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, '#section2Content p')

    THIRD_SECTION = (By.CSS_SELECTOR, '#section3Heading')
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, '#section3Content p')


class AutoCompletePageLocators:
    """Class for Auto Complete page locators."""
    MULTIPLE_INPUT = (By.CSS_SELECTOR, '#autoCompleteMultipleInput')
    MULTIPLE_INPUT_ITEMS = (By.CSS_SELECTOR, '.auto-complete__multi-value')
    MULTIPLE_INPUT_ITEM_DELETE = (By.CSS_SELECTOR, '.auto-complete__multi-value path')
    MULTIPLE_INPUT_CLEAR_BUTTON = (By.CSS_SELECTOR, '.auto-complete__clear-indicator')

    SINGLE_INPUT = (By.CSS_SELECTOR, '#autoCompleteSingleInput')
    SINGLE_INPUT_ITEM = (By.CSS_SELECTOR, '.css-1uccc91-singleValue')


class DatePickerPageLocators:
    """Class for Date Picker page locators."""
    DATE_INPUT = (By.CSS_SELECTOR, '#datePickerMonthYearInput')
    DATE_MONTH_SELECT = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    DATE_YEAR_SELECT = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    DATE_AVAILABLE_DAYS = (By.CSS_SELECTOR, '.react-datepicker__day')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, '#dateAndTimePickerInput')
    DATE_AND_TIME_MONTH_VIEW = (By.CSS_SELECTOR, '.react-datepicker__month-read-view')
    DATE_AND_TIME_AVAILABLE_MONTHS = (By.CSS_SELECTOR, '.react-datepicker__month-option')
    DATE_AND_TIME_YEAR_VIEW = (By.CSS_SELECTOR, '.react-datepicker__year-read-view')
    DATE_AND_TIME_AVAILABLE_YEARS = (By.CSS_SELECTOR, '.react-datepicker__year-option')
    DATE_AND_TIME_AVAILABLE_TIMES = (By.CSS_SELECTOR, '.react-datepicker__time-list-item')


class SliderPageLocators:
    """Class for Slider page locators."""
    SLIDER_INPUT = (By.CSS_SELECTOR, '.range-slider')
    SLIDER_VALUE = (By.CSS_SELECTOR, '#sliderValue')
