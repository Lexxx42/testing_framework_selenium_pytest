"""This module represents base page object with shared methods for all pages."""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    """Base class for web page objects."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self) -> None:
        """Open the page."""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Returns element if it's visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Returns list of elements if they are visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Returns element if it's present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Returns list of elements if they are present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """
        Returns element if it's invisible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Returns element if it's clickable.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element) -> bool:
        """
        Set's the focus of driver to the element with JS code.
        :returns: False if no element to go to.
        """
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True

    def perform_double_click(self, locator):
        """
        Perform double-click on an element.
        :param locator: locator of web element.
        """
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(locator)).double_click().perform()

    def perform_right_click(self, locator):
        """
        Perform right-click on an element.
        :param locator: locator of web element.
        """
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(locator)).context_click().perform()

    def perform_dynamic_click(self, locator):
        """
        Perform left-click on an element.
        :param locator: locator of web element.
        """
        self.element_is_visible(locator).click()

    def switch_to_new_tab(self):
        """
        Switch focus of driver to the new tab.
        """
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self) -> str:
        """
        Get the current URL.
        :return: current URL of active window.
        """
        return self.driver.current_url

    def remove_footer(self):
        """Remove footer with JS code to perform tests."""
        self.driver.execute_script('document.getElementsByTagName(\'footer\')[0].remove();')
        self.driver.execute_script('document.getElementById(\'close-fixedban\').remove();')

    def get_alert_text(self, timeout=6, is_accepted=True, data=None) -> str:
        """Switch focus of driver to alert.
        :param timeout: time delay for search the element.
        :param is_accepted: is the alert accepted of not.
        :param data: text to pass in the alert textbox.
        :returns: text of the alert message.
        """
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        try:
            if data:
                alert.send_keys(data)
            alert_text = alert.text
        finally:
            if is_accepted:
                alert.accept()
            else:
                alert.dismiss()
        return alert_text

    def switch_to_frame(self, frame_locator, timeout=5):
        """
        Switch focus of driver to frame.
        :param frame_locator: locator for frame to switch to.
        :param timeout: time delay for search the element.
        """
        wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def is_element_disappeared(self, locator, timeout=1) -> bool:
        """
        Check if element is disappeared.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        :returns: True if element is disappeared.
        """
        try:
            wait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, locator, timeout=5) -> bool:
        """
        Check if element is visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        :returns: True if element is visible.
        """
        try:
            self.go_to_element(self.element_is_present(locator))
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def select_date_by_text(self, element, text) -> None:
        """
        Selects a date by visible text.
        :param element: Element to select.
        :param text: Text to select.
        """
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(text)

    def select_element_from_elements_by_text(self, elements, text) -> None:
        """
        Selects an element by visible text.
        :param elements: Elements to select from.
        :param text: Text to select.
        """
        elements_to_pick_from = self.elements_are_present(elements)
        for element in elements_to_pick_from:
            if element.text == text:
                element.click()
                break

    def drag_and_drop_by_offset(self, element, x_coordinate, y_coordinate) -> None:
        """Holds left mouse button and drags the element to the x, y coordinates."""
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coordinate, y_coordinate)
        action.perform()

    def drag_and_drop_to_element(self, from_what, to_where) -> None:
        """
        Drags element to certain position of another element.
        :param from_what: What element to drag.
        :param to_where: Where to drag element.
        """
        action = ActionChains(self.driver)
        action.drag_and_drop(from_what, to_where)
        action.perform()

    def move_cursor_to_center_of_element(self, element) -> None:
        """Moves cursor to center of element."""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
