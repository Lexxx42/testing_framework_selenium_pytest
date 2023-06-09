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
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..locators import TextBoxPageLocators, CheckBoxPageLocators, \
    RadioButtonPageLocators, WebTablePageLocators, \
    ButtonsPageLocators, LinksPageLocators, \
    BrokenLinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from ..generator import generated_person, generated_file


class TextBoxPage(BasePage):
    """Text Box page object."""
    locators = TextBoxPageLocators()

    @allure.step('Fill all form fields with generated data.')
    def fill_all_fields(self) -> tuple[str, str, str, str]:
        """
        Fill all form fields with generated data.
        :returns: Filled full name, email, current and permanent address.
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Fill name'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        with allure.step('Fill email'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
        with allure.step('Fill current address'):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        with allure.step('Fill permanent address'):
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('Fill click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Check output data of sent form.')
    def check_filled_form(self) -> tuple[str, str, str, str]:
        """
        Check output data of sent form.
        :returns: Form's data: full name, email, current and permanent address.
        """
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text.split(':')[-1]
        email = self.element_is_present(
            self.locators.CREATED_EMAIL).text.split(':')[-1]
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[-1]
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[-1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """Check Box page object."""
    locators = CheckBoxPageLocators()

    @allure.step('Open dropdown list.')
    def open_fill_list(self) -> None:
        """Open dropdown list."""
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Activate random checkboxes.')
    def click_random_checkbox(self) -> None:
        """Activates random checkboxes."""
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count > 0:
            item = item_list[randint(0, len(item_list) - 1)]
            self.go_to_element(item)
            item.click()
            count -= 1

    @allure.step('Returns activated checkboxes text.')
    def get_checked_checkboxes(self) -> str:
        """
        Returns activated checkboxes text.
        :returns: Text of activated checkboxes.
        """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = [checkbox.find_element(
            'xpath', self.locators.TITLE_CHECKBOX).text for checkbox in checked_list]
        return str(data).replace(' ', '').replace('.doc', '').lower()

    @allure.step('Returns output result of active checkboxes.')
    def get_output_result(self) -> str:
        """
        Returns output result of active checkboxes.
        :returns: Text output of active checkboxes.
        """
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT_LIST)
        data = [item.text for item in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    """Radio Button page object."""
    locators = RadioButtonPageLocators()

    @allure.step('Click on radio button.')
    def click_on_the_radio_button(self, choice) -> None:
        """Click on radio button."""
        choices = {
            'yes': self.locators.RADIO_BUTTON_YES,
            'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
            'no': self.locators.RADIO_BUTTON_NO
        }
        with allure.step(f'Click on radio button {choice}'):
            self.element_is_visible(choices[choice]).click()

    @allure.step('Returns output result of active radio button.')
    def get_radiobutton_output_result(self) -> str:
        """
        Returns output result of active radio button.
        :returns: Text output result of active radio button.
        """
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    """Web Tables page object."""
    locators = WebTablePageLocators()

    @allure.step('Adds count numbers of persons with generated data to the table.')
    def add_new_person_to_the_table(self, count=1) -> list[str, str, int, str, int, str]:
        """
        Adds count numbers of persons with generated data to the table.
        :param count: Number of persons to be added to the table.
        :returns: List of person's data sent to the table.
        """
        first_name = ''
        last_name = ''
        age = -1
        email = ''
        salary = -1
        department = ''
        while count > 0:
            with allure.step('Generate person info'):
                person_info = next(generated_person())
                first_name = person_info.first_name
                last_name = person_info.last_name
                age = person_info.age
                email = person_info.email
                salary = person_info.salary
                department = person_info.department
            with allure.step('Click on add button'):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
            with allure.step('Fill first name'):
                self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
            with allure.step('Fill last name'):
                self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(last_name)
            with allure.step('Fill email'):
                self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
            with allure.step('Fill age'):
                self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
            with allure.step('Fill salary'):
                self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)
            with allure.step('Fill department'):
                self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)
            with allure.step('Click submit button'):
                self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Returns current persons from the table.')
    def get_current_persons_in_table(self) -> list:
        """
        Returns current persons from the table.
        :returns: current persons from the table.
        """
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    @allure.step('Searches for a person with a key_word in a table.')
    def search_some_person(self, key_word) -> None:
        """
        Searches for a person with a key_word in a table.
        :param key_word: Keyword to search with.
        """
        search_field = self.element_is_visible(self.locators.SEARCH_FIELD)
        search_field.click()
        with allure.step(f'Search person with {key_word=}'):
            search_field.send_keys(key_word)

    @allure.step('Check search result.')
    def check_search_person(self) -> list[str]:
        """
        Check search result.
        :returns: List of search result.
        """
        delete_button = self.element_is_clickable(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person info in the table.')
    def update_person_info(self, field_to_edit='age') -> str:
        """
        Update person info in the table.
        :param field_to_edit: Field of table to be edited.
        :returns: Edited info.
        """
        person_info = next(generated_person())
        edited_data = getattr(person_info, field_to_edit)
        with allure.step('Click on update button'):
            self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        locator = getattr(self.locators, field_to_edit.upper() + '_FIELD')
        with allure.step('Clear search field before search'):
            self.element_is_visible(locator).clear()
        with allure.step(f'Sending {edited_data=} of person\'s {field_to_edit=}'):
            self.element_is_visible(locator).send_keys(edited_data)
        with allure.step('Click on submit button'):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(edited_data)

    @allure.step('Delete person info from the table.')
    def delete_person(self):
        """Delete person info from the table."""
        with allure.step('Click on delete button'):
            self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check search result message.')
    def check_search_result_message(self) -> str:
        """
        Check search result message.
        :returns: Search result message.
        """
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Change table row count appearance.')
    def select_numer_of_rows(self) -> list[int]:
        """
        Change table row count appearance.
        :returns: Number of rows available for user to click to.
        """
        number_of_rows = [5, 10, 20, 25, 50, 100]
        can_be_selected_numbers_of_row = []
        for number in number_of_rows:
            with allure.step('Check if button to change row number is clickable'):
                change_number_of_rows_button = \
                    self.element_is_clickable(self.locators.SELECT_NUMBER_OF_ROWS)
            with allure.step('Click on button of row number selection'):
                change_number_of_rows_button.click()
            with allure.step(f'Check if selection of {number} is available'):
                self.element_is_visible((By.CSS_SELECTOR, f'option[value=\'{number}\']')).click()
            with allure.step(f'Add available {number} to comparison list'):
                can_be_selected_numbers_of_row.append(self.check_number_of_rows())
        return can_be_selected_numbers_of_row

    @allure.step('Check row count appearance.')
    def check_number_of_rows(self) -> int:
        """
        Check row count appearance.
        :returns: Numbers of rows.
        """
        return len(self.elements_are_present(self.locators.FULL_PEOPLE_LIST))


class ButtonsPage(BasePage):
    """Buttons page object."""
    locators = ButtonsPageLocators()

    @allure.step('Performs double-click on element.')
    def perform_double_click(self, locator=None):
        """
        Performs double-click on element.
        :param locator: Locator of web element.
        """
        super().perform_double_click(self.locators.DOUBLE_CLICK_ME_BUTTON)

    @allure.step('Performs right-click on element.')
    def perform_right_click(self, locator=None):
        """
        Performs right-click on element.
        :param locator: Locator of web element.
        """
        super().perform_right_click(self.locators.RIGHT_CLICK_ME_BUTTON)

    @allure.step('Performs left-click on element.')
    def perform_dynamic_click(self, locator=None):
        """
        Performs dynamic-click on element.
        :param locator: Locator of web element.
        """
        super().perform_dynamic_click(self.locators.CLICK_ME_BUTTON)

    @allure.step('Check dynamic-click result message.')
    def get_dynamic_click_message(self):
        """
        Check dynamic-click result message.
        :returns: Message text.
        """
        return self.element_is_present(self.locators.CLICK_MESSAGE).text

    @allure.step('Check double-click result message.')
    def get_double_click_message(self):
        """
        Check double-click result message.
        :returns: Message text.
        """
        return self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text

    @allure.step('Check right-click result message.')
    def get_right_click_message(self):
        """
        Check right-click result message.
        :returns: Message text.
        """
        return self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text


class LinksPage(BasePage):
    """Links page object."""
    locators = LinksPageLocators()
    NO_ERRORS = 'No errors'

    @allure.step('Check if new tab is opened.')
    def check_new_tab_simple_link(self) -> tuple[str, str]:
        """
        Check if new tab is opened.
        :returns: Found link in DOM,
            url of new tab or error message if nothing to go to.
        """
        with allure.step('Get link href'):
            simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
            link_href = simple_link.get_attribute('href')
        try:
            with allure.step(f'Get request with a {link_href=}'):
                requests.get(link_href, timeout=5)
                simple_link.click()
            with allure.step('Switch to new tab'):
                self.switch_to_new_tab()
            with allure.step('Get URL from current tab'):
                url = self.get_current_url()
        except requests.exceptions.RequestException as error:
            return link_href, str(error)
        return link_href, url

    @allure.step('Check broken link status code.')
    def check_broken_link(self, url) -> tuple:
        """
        Check broken link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on bad request link'):
                self.element_is_present(self.locators.BAD_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, str(error)
        return request.status_code, self.NO_ERRORS

    @allure.step('Check if new tab is opened on dynamic link.')
    def check_new_tab_dynamic_link(self) -> tuple[str, str]:
        """
        Check if new tab is opened on dynamic link.
        :returns: Found link in DOM,
            url of new tab or error message if nothing to go to.
        """
        with allure.step('Get link href'):
            simple_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
            link_href = simple_link.get_attribute('href')
        try:
            with allure.step(f'Get request with a {link_href=}'):
                requests.get(link_href, timeout=5)
                simple_link.click()
            with allure.step('Switch to new tab'):
                self.switch_to_new_tab()
            with allure.step('Get URL from current tab'):
                url = self.get_current_url()
        except requests.exceptions.RequestException as error:
            return link_href, str(error)
        return link_href, url

    @allure.step('Check created link status code.')
    def check_created_link(self, url) -> tuple:
        """
        Check created link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on created request link'):
                self.element_is_present(self.locators.CREATED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS

    @allure.step('Check no content link status code.')
    def check_no_content_link(self, url) -> tuple:
        """
        Check no content link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on no content link'):
                self.element_is_present(self.locators.NO_CONTENT_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS

    @allure.step('Check moved link status code.')
    def check_moved_link(self, url) -> tuple:
        """
        Check moved link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on moved request link'):
                self.element_is_present(self.locators.MOVED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS

    @allure.step('Check unauthorized link status code.')
    def check_unauthorized_link(self, url) -> tuple:
        """
        Check unauthorized link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on unauthorized request link'):
                self.element_is_present(self.locators.UNAUTHORIZED_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS

    @allure.step('Check forbidden link status code.')
    def check_forbidden_link(self, url) -> tuple:
        """
        Check forbidden link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on forbidden request link'):
                self.element_is_present(self.locators.FORBIDDEN_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS

    @allure.step('Check not found link status code.')
    def check_not_found_link(self, url) -> tuple:
        """
        Check not found link status code.
        :param url: URL to check.
        :returns: Request and error message
            if error when getting response.
            Request status code and no errors message
            if no errors when getting response.
        """
        request = -1
        try:
            with allure.step(f'Get request with {url=}'):
                request = requests.get(url, timeout=5)
            with allure.step('Click on not found link request link'):
                self.element_is_present(self.locators.NOT_FOUND_REQUEST).click()
        except requests.exceptions.RequestException as error:
            return request, error
        return request.status_code, self.NO_ERRORS


class BrokenLinksPage(BasePage):
    """Broken Links page object."""
    locators = BrokenLinksPageLocators()
    NO_ERRORS = 'No errors'

    @allure.step('Check valid image status code and content type.')
    def check_valid_image_for_200_response_and_content_type(self) -> tuple:
        """
        Check valid image status code and content type.
        :returns: Status code and content type
            if no error when checking image status code.
            Request, content type and error message
            if error occurred when checking image status code.
        """
        image = self.element_is_visible(self.locators.VALID_IMAGE)
        content_type = None
        request = -1
        try:
            with allure.step('Get image link from src attribute'):
                image_link = image.get_attribute('src')
            with allure.step(f'Get request with {image_link=}'):
                request = requests.get(image_link, timeout=5)
            with allure.step('Get image content type'):
                content_type = request.headers.get('content-type')
        except requests.exceptions.RequestException as error:
            return request, content_type, error
        return request.status_code, content_type, self.NO_ERRORS

    @allure.step('Check broken image status code and content type.')
    def check_broken_image_for_200_response_and_content_type(self) -> tuple:
        """
        Check broken image status code and content type.
        :returns: Status code and content type
            if no error when checking image status code.
            Request, content type and error message
            if error occurred when checking image status code.
        """
        with allure.step('Get image link from src attribute'):
            image = self.element_is_visible(self.locators.BROKEN_IMAGE)
            image_link = image.get_attribute('src')
        request = -1
        content_type = None
        try:
            with allure.step(f'Get request with {image_link=}'):
                request = requests.get(image_link, timeout=5)
            with allure.step('Get image content type'):
                content_type = request.headers.get('content-type')
        except requests.exceptions.RequestException as error:
            return request, content_type, error
        return request.status_code, content_type, self.NO_ERRORS

    @allure.step('Check valid link href and url.')
    def check_valid_link(self) -> tuple[str, str]:
        """
        Check valid link href and url.
        :returns: Link href from DOM and current URL
            if no errors occurred.
            Link href from DOM and error message
            if error occurred.
        """
        with allure.step('Get link href'):
            valid_link = self.element_is_visible(self.locators.VALID_LINK)
            link_href = valid_link.get_attribute('href')
        try:
            with allure.step(f'Get request with {link_href=}'):
                page = requests.get(link_href, timeout=5)
            with allure.step('Click on a link'):
                valid_link.click()
            with allure.step('Get current page URL'):
                url = page.url
        except requests.exceptions.RequestException as error:
            return link_href.split('/')[2], str(error)
        return link_href.split('/')[2], url.split('/')[2]

    @allure.step('Check broken link status code and url.')
    def check_broken_link(self) -> tuple:
        """
        Check broken link status code and url.
        :returns: Page status code and current URL
            if no errors occurred.
            Page, current URL and error message
            if error occurred.
        """
        with allure.step('Get link href'):
            broken_link = self.element_is_visible(self.locators.BROKEN_LINK)
            link_href = broken_link.get_attribute('href')
        page = -1
        url = -1
        try:
            with allure.step(f'Get request with {link_href=}'):
                page = requests.get(link_href, timeout=5)
            with allure.step('Click on a broken link'):
                broken_link.click()
            with allure.step('Get current page URL'):
                url = page.url
        except requests.exceptions.RequestException as error:
            return page, url, error
        return page.status_code, url, self.NO_ERRORS


class UploadAndDownloadPage(BasePage):
    """Upload and Download page object."""
    locators = UploadAndDownloadPageLocators()

    @allure.step('Uploads file. Returns filename and upload text result.')
    def upload_file(self) -> tuple:
        """
        Uploads file. Returns filename and upload text result.
        :returns: Filename, uploaded file text
            if no errors occurred.
            None, error message
            if error occurred.
        """
        file_name, file_path = generated_file()
        try:
            with allure.step('Uploads file'):
                self.element_is_visible(self.locators.UPLOAD_FILE_BUTTON).send_keys(file_path)
            with allure.step('Returns filename and upload text result'):
                upload_file_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
                remove(file_path)
        except FileNotFoundError as error:
            return None, error
        return file_name, upload_file_text.split('\\')[-1]

    @allure.step('Downloads file. Returns True if file downloaded.')
    def is_file_downloaded(self) -> bool | FileNotFoundError:
        """
        Downloads file. Returns True if file downloaded.
        :returns: True if file downloaded
            False if isn't downloaded.
        """
        try:
            with allure.step('Get link from href'):
                link = self.element_is_visible(
                    self.locators.DOWNLOAD_FILE_BUTTON).get_attribute('href')
            with allure.step('Get byte info from link'):
                link_bytes = base64.b64decode(link)
            with allure.step('Creating file for writing image data'):
                file_name = f'filetest{randint(0, 999)}.jpg'
                file_path = path.abspath(file_name)
            with allure.step('Writing image data'):
                with open(file_name, 'wb+') as file:
                    offset = link_bytes.find(b'\xff\xd8')
                    file.write(link_bytes[offset:])
            with allure.step('Check if file exists'):
                check_file = path.exists(file_path)
            with allure.step('Remove file'):
                remove(file_path)
        except FileNotFoundError as error:
            return error
        return check_file


class DynamicPropertiesPage(BasePage):
    """Dynamic Properties page object."""
    locators = DynamicPropertiesPageLocators()

    @allure.step('Returns if button was enabled or not.')
    def is_button_enabled(self) -> bool:
        """
        Returns if button was enabled or not.
        :returns: True if button was enabled.
            False if button wasn't enabled.
        """
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Checks change of color of the button.')
    def check_change_of_color(self):
        """
        Checks change of color of the button.
        """
        color_button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON)
        with allure.step('Get color before changing'):
            color_before = color_button.value_of_css_property('color')
        time.sleep(5)  # TODO: refactor with wait() instead.
        with allure.step('Get color after changing'):
            color_after = color_button.value_of_css_property('color')
        return color_before, color_after

    @allure.step('Checks button appearance.')
    def is_button_appeared(self) -> bool:
        """
        Checks button appearance.
        :returns: True if button appeared.
            False if isn't appeared.
        """
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON, 1)
        except TimeoutException:
            return False
        return True
