from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except (NoSuchElementException):
            return False
        return True

    def perform_double_click(self):
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BUTTON)).double_click().perform()

    def perform_right_click(self):
        action_chains = ActionChains(self.driver)
        action_chains.context_click(
            self.element_is_visible(self.locators.RIGHT_CLICK_ME_BUTTON)).context_click().perform()

    def perform_dynamic_click(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url

    def zoom_page(self, zoom: float):
        self.driver.execute_script(f'document.body.style.zoom = \'{zoom}\'')

    def remove_footer(self):
        self.driver.execute_script('document.getElementsByTagName(\'footer\')[0].remove();')
        self.driver.execute_script('document.getElementById(\'close-fixedban\').remove();')

    def switch_to_alert(self, timeout=6, is_accepted=True):
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        try:
            alert_text = alert.text
        finally:
            if is_accepted:
                alert.accept()
            else:
                alert.dismiss()
        return alert_text
