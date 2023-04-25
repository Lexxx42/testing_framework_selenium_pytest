"""This module represents base page object with shared methods for all pages."""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    """Base class for web page objects."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Open the page."""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Returns element if it's visible."""
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """Returns list of elements if they are visible."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """Returns element if it's present in page DOM."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """Returns list of elements if they are present in page DOM."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """Returns element if it's invisible."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """Returns element if it's clickable."""
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """Set's the focus of driver to the element with JS code."""
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True

    def perform_double_click(self, locator):
        """Perform double-click on an element."""
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(locator)).double_click().perform()

    def perform_right_click(self, locator):
        """Perform right-click on an element."""
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(locator)).context_click().perform()

    def perform_dynamic_click(self, locator):
        """Perform left-click on an element."""
        self.element_is_visible(locator).click()

    def switch_to_new_tab(self):
        """Switch focus of driver to the new tab."""
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url

    def zoom_page(self, zoom: float):
        """Zoom page in or out with JS code."""
        self.driver.execute_script(f'document.body.style.zoom = \'{zoom}\'')

    def remove_footer(self):
        """Remove footer with JS code to perform tests."""
        self.driver.execute_script('document.getElementsByTagName(\'footer\')[0].remove();')
        self.driver.execute_script('document.getElementById(\'close-fixedban\').remove();')

    def switch_to_alert(self, timeout=6, is_accepted=True, data=None):
        """Switch focus of driver to alert."""
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
        """Switch focus of driver to frame."""
        wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def is_element_disappeared(self, locator, timeout=1):
        """Check if element is disappeared."""
        try:
            wait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible."""
        try:
            self.go_to_element(self.element_is_present(locator))
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False
        return True
