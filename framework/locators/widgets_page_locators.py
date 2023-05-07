"""This module contains locators for Widgets tab on the site.

Contains locators for following tabs:
Accordian,
Auto Complete,
Date Picker,
Slider,
Progress Bar,
Tabs,
Tool Tips
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


class ProgressBarPageLocators:
    """Class for Progress Bar page locators."""
    START_STOP_BUTTON = (By.CSS_SELECTOR, '#startStopButton')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, '.progress-bar')


class TabsPageLocators:
    """Class for Tabs page locators."""
    TAB_WHAT = (By.CSS_SELECTOR, '#demo-tab-what')
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-what .mt-3')
    TAB_ORIGIN = (By.CSS_SELECTOR, '#demo-tab-origin')
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-origin .mt-3')
    TAB_USE = (By.CSS_SELECTOR, '#demo-tab-use')
    TAB_USE_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-use .mt-3')
    TAB_MORE = (By.CSS_SELECTOR, '#demo-tabpane-more')
    TAB_MORE_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-more .mt-3')


class ToolTipsPageLocators:
    """Class for Tool Tips page locators."""
    BUTTON = (By.CSS_SELECTOR, '#toolTipButton')
    TOOLTIP_BUTTON = (By.CSS_SELECTOR, '[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, '#toolTipTextField')
    TOOLTIP_FIELD = (By.CSS_SELECTOR, '[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.CSS_SELECTOR, '#texToolTopContainer a:nth-child(1)')
    TOOLTIP_CONTRARY_LINK = (By.CSS_SELECTOR, '[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.CSS_SELECTOR, '#texToolTopContainer a:nth-child(2)')
    TOOLTIP_SECTION_LINK = (By.CSS_SELECTOR, '[aria-describedby="sectionToolTip"]')

    TOOLTIPS_INNERS = (By.CSS_SELECTOR, '.tooltip-inner')
