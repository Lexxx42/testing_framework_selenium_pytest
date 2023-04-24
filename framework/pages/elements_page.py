"""Module contains tests for Elements tab on the site.

Contains page objects for:
Text Box,
Check Box,
Radio Button,
Web Tables,
Buttons,
Links,
Broken Links - Images,
Upload and Download,
Dynamic Properties.
"""
import base64
import time
from os import remove, path
from random import randint
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, WebTablePageLocators, \
    ButtonsPageLocators, LinksPageLocators, BrokenLinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from ..generator import generated_person, generated_file


class TextBoxPage(BasePage):
    """Text Box page object."""
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Fill all form fields with generated data."""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """Check output data of sent form."""
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[-1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[-1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[-1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[-1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """Check Box page object."""
    locators = CheckBoxPageLocators()

    def open_fill_list(self):
        """Open dropdown list."""
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """Activates random checkboxes."""
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count > 0:
            item = item_list[randint(0, len(item_list) - 1)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        """Returns activated checkboxes text."""
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = [checkbox.find_element('xpath', self.locators.TITLE_CHECKBOX).text for checkbox in checked_list]
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        """Returns output result of active checkboxes."""
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT_LIST)
        data = [item.text for item in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    """Radio Button page object."""
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        """Click on radio button."""
        choices = {'yes': self.locators.RADIO_BUTTON_YES, 'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
                   'no': self.locators.RADIO_BUTTON_NO}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        """Returns output result of active radio button."""
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    """Web Tables page object."""
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        """Adds count numbers of persons with generated data to the table."""
        while count > 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            age = person_info.age
            email = person_info.email
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
            self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        """Returns list of persons from the table."""
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    def search_some_person(self, key_word):
        """Searches for a person with a key_word in a table."""
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def check_search_person(self):
        """Check search result."""
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self, field_to_edit='age'):
        """Update person info in the table."""
        person_info = next(generated_person())
        edited_data = getattr(person_info, field_to_edit)
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        locator = getattr(self.locators, field_to_edit.upper() + '_FIELD')
        self.element_is_visible(locator).clear()
        self.element_is_visible(locator).send_keys(edited_data)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(edited_data)

    def delete_person(self):
        """Delete person info from the table."""
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_delete(self):
        """Check if person info deleted from the table."""
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_numer_of_rows(self):
        """Change table row count appearance."""
        number_of_rows = [5, 10, 20, 25, 50, 100]
        data = []
        for number in number_of_rows:
            change_number_of_rows_button = self.element_is_visible(self.locators.SELECT_NUMBER_OF_ROWS)
            self.go_to_element(change_number_of_rows_button)
            change_number_of_rows_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value=\'{number}\']')).click()
            data.append(self.check_count_of_rows())
        return data

    def check_count_of_rows(self):
        """Check row count appearance."""
        return len(self.elements_are_present(self.locators.FULL_PEOPLE_LIST))


class ButtonsPage(BasePage):
    """Buttons page object."""
    locators = ButtonsPageLocators()

    def perform_double_click(self, locator=None):
        """Performs double-click on element."""
        super().perform_double_click(self.locators.DOUBLE_CLICK_ME_BUTTON)

    def perform_right_click(self, locator=None):
        """Performs right-click on element."""
        super().perform_right_click(self.locators.RIGHT_CLICK_ME_BUTTON)

    def perform_dynamic_click(self, locator=None):
        """Performs dynamic-click on element."""
        super().perform_dynamic_click(self.locators.CLICK_ME_BUTTON)

    def check_dynamic_click_message(self):
        """Check dynamic-click result message."""
        return self.element_is_present(self.locators.CLICK_MESSAGE).text

    def check_double_click_message(self):
        """Check double-click result message."""
        return self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text

    def check_right_click_message(self):
        """Check right-click result message."""
        return self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text


class LinksPage(BasePage):
    """Links page object."""
    locators = LinksPageLocators()
    NO_ERRORS = 'No errors'

    def check_new_tab_simple_link(self):
        """Check if new tab is opened."""
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        try:
            requests.get(link_href)
            simple_link.click()
            url = self.switch_to_new_tab()
        except requests.exceptions.RequestException as error:
            return link_href, error
        return link_href, url

    def check_broken_link(self, url):
        """Check broken link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.BAD_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_new_tab_dynamic_link(self):
        """Check if new tab is opened on dynamic link."""
        simple_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = simple_link.get_attribute('href')
        try:
            requests.get(link_href)
            simple_link.click()
            url = self.switch_to_new_tab()
        except requests.exceptions.RequestException as error:
            return link_href, error
        return link_href, url

    def check_created_link(self, url):
        """Check created link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.CREATED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_no_content_link(self, url):
        """Check no content link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.NO_CONTENT_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_moved_link(self, url):
        """Check moved link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.MOVED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_unauthorized_link(self, url):
        """Check unauthorized link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.UNAUTHORIZED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_forbidden_link(self, url):
        """Check forbidden link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.FORBIDDEN_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS

    def check_not_found_link(self, url):
        """Check not found link status code."""
        try:
            request = requests.get(url)
            self.element_is_present(self.locators.NOT_FOUND_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request.status_code, error
        return request.status_code, self.NO_ERRORS


class BrokenLinksPage(BasePage):
    """Broken Links page object."""
    locators = BrokenLinksPageLocators()
    NO_ERRORS = 'No errors'

    def check_valid_image_for_200_response(self):
        """Check valid image status code and content type."""
        image = self.element_is_visible(self.locators.VALID_IMAGE)
        try:
            image_link = image.get_attribute('src')
            request = requests.get(image_link)
            content_type = request.headers.get('content-type')
        except requests.exceptions.RequestException as error:
            return request.status_code, content_type, error
        return request.status_code, content_type, self.NO_ERRORS

    def check_broken_image_for_200_response(self):
        """Check broken image status code and content type."""
        image = self.element_is_visible(self.locators.BROKEN_IMAGE)
        image_link = image.get_attribute('src')
        try:
            request = requests.get(image_link)
            content_type = request.headers.get('content-type')
        except requests.exceptions.RequestException as error:
            return request.status_code, content_type, error
        return request.status_code, content_type, self.NO_ERRORS

    def check_valid_link(self):
        """Check valid link href and url."""
        valid_link = self.element_is_visible(self.locators.VALID_LINK)
        link_href = valid_link.get_attribute('href')
        try:
            page = requests.get(link_href)
            valid_link.click()
            url = page.url
        except requests.exceptions.RequestException as error:
            return link_href.split('/')[2], error
        return link_href.split('/')[2], url.split('/')[2]

    def check_broken_link(self):
        """Check broken link status code and url."""
        broken_link = self.element_is_visible(self.locators.BROKEN_LINK)
        link_href = broken_link.get_attribute('href')
        try:
            page = requests.get(link_href)
            broken_link.click()
            url = page.url
        except requests.exceptions.RequestException as error:
            return page.status_code, url, error
        return page.status_code, url, self.NO_ERRORS


class UploadAndDownloadPage(BasePage):
    """Upload and Download page object."""
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        """Uploads file. Returns filename and upload text result."""
        file_name, path = generated_file()
        try:
            self.element_is_visible(self.locators.UPLOAD_FILE_BUTTON).send_keys(path)
            upload_file_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
            remove(path)
        except FileNotFoundError as e:
            return None, e
        return file_name, upload_file_text.split('\\')[-1]

    def download_file(self):
        """Downloads file. Returns generated file."""
        try:
            link = self.element_is_visible(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')
            link_bytes = base64.b64decode(link)
            file_name = f'filetest{randint(0, 999)}.jpg'
            file_path = path.abspath(file_name)
            with open(file_name, 'wb+') as f:
                offset = link_bytes.find(b'\xff\xd8')
                f.write(link_bytes[offset:])
            check_file = path.exists(file_path)
            remove(file_path)
        except FileNotFoundError as e:
            return e
        return check_file


class DynamicPropertiesPage(BasePage):
    """Dynamic Properties page object."""
    locators = DynamicPropertiesPageLocators()

    def check_enabled_button(self):
        """Returns if button was enabled or not."""
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_change_of_color(self):
        """Checks change of color of the button."""
        color_button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON)
        color_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_after = color_button.value_of_css_property('color')
        return color_before, color_after

    def check_button_appearance(self):
        """Checks button appearance."""
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON, 1)
        except TimeoutException:
            return False
        return True
