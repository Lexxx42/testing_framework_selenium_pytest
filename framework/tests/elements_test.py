"""Module contains tests for Elements tab on the site.

Contains tabs:
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
from random import randint, choice
import allure
import pytest
from ..pages import TextBoxPage, CheckBoxPage, \
    RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    BrokenLinksPage, UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite('Elements tab')
class TestElements:
    """Class represents Elements tab.
    Contains tabs:
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

    @allure.feature('Text Box')
    class TestTextBox:
        """Class represents Text Box tab tests."""

        @allure.title('Test user can fill the form and sent it.')
        def test_text_box(self, driver):
            """Test user can fill the form and sent it."""
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, \
                output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, \
                f'Entered full name was {full_name} ' \
                f'which doesn\'t match output full name {output_name}'
            assert email == output_email, \
                f'Entered email was {email} ' \
                f'which doesn\'t match output email {output_email}'
            assert current_address == output_current_address, \
                f'Entered current address was {current_address} ' \
                f'which doesn\'t match output current address {output_current_address}'
            assert permanent_address == output_permanent_address, \
                f'Entered permanent address was {permanent_address} ' \
                f'which doesn\'t match output permanent address {output_permanent_address}'

    @allure.feature('Check Box')
    class TestCheckBox:
        """Class represents Check Box tab tests."""

        @allure.title('Test user can select checkboxes.')
        def test_check_box(self, driver):
            """Test user can select checkboxes."""
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_fill_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, \
                f'Checked checkboxes {input_checkboxes} ' \
                f'are not matching output result checkboxes {output_result}'

    @allure.feature('Radio Button')
    class TestRadioButton:
        """Class represents Radio Button tab tests."""

        @allure.title('Test user can select radio buttons.')
        @pytest.mark.parametrize('action', ['yes', 'impressive', 'no'])
        def test_radio_button(self, driver, action: str):
            """Test user can select radio buttons."""
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button(action)
            output = radio_button_page.get_radiobutton_output_result()
            assert action.title() == output, f'Action {action} don\'t match the result {output}'

    @allure.feature('Web Table')
    class TestWebTable:
        """Class represents Web Tables tab tests."""
        web_page_link = 'https://demoqa.com/webtables'

        @allure.title('Test user can add person to the table.')
        def test_web_table_add_person(self, driver):
            """Test user can add person to the table."""
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            new_person = web_table_page.add_new_person_to_the_table(1)
            table = web_table_page.get_current_persons_in_table()
            assert new_person in table, \
                f'New person {new_person} should be in the table {table} but it isn\'t'

        @allure.title('Test user can search person in the table.')
        def test_web_table_search_person(self, driver):
            """Test user can search person in the table."""
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            key_word = web_table_page.add_new_person_to_the_table()[randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, \
                f'Person was not found by key word {key_word} in table {table_result}'

        @allure.title('Test user can update person info in the table.')
        def test_web_table_update_person_info(self, driver):
            """Test user can update person info in the table."""
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            fields_to_edit = ['first_name', 'last_name',
                              'age', 'salary', 'department', 'email']
            field_to_edit = choice(fields_to_edit)
            last_name = web_table_page.add_new_person_to_the_table()[1]
            web_table_page.search_some_person(last_name)
            edited_field = web_table_page.update_person_info(field_to_edit)
            row = web_table_page.check_search_person()
            assert edited_field in row, \
                f'Edited person info {edited_field} in ' \
                f'{fields_to_edit} not present in edited data {row}'

        @allure.title('Test user can delete person from the table.')
        def test_web_table_delete_person(self, driver):
            """Test user can delete person from the table."""
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            email = web_table_page.add_new_person_to_the_table()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_search_result_message()
            search_results_message = 'No rows found'
            assert text == search_results_message, \
                f'Text of search result of deleted person' \
                f' must be \'{search_results_message}\' but {text} present'

        @allure.title('Test user can change number of rows in the table.')
        def test_table_change_number_of_rows(self, driver):
            """Test user can change number of rows in the table."""
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            number_of_rows = web_table_page.select_numer_of_rows()
            available_number_of_rows = [5, 10, 20, 25, 50, 100]
            assert number_of_rows == available_number_of_rows, \
                f'Available rows count is {available_number_of_rows}' \
                f' expected but got {number_of_rows}'

    @allure.feature('Buttons')
    class TestButtons:
        """Class represents Buttons tab tests."""
        buttons_page_link = 'https://demoqa.com/buttons'

        @allure.title('Test user can left mouse click on a button.')
        def test_dynamic_click_on_the_button_click_me(self, driver):
            """Test user can left mouse click on a button."""
            buttons_page = ButtonsPage(driver, self.buttons_page_link)
            buttons_page.open()
            buttons_page.perform_dynamic_click()
            click_message = buttons_page.get_dynamic_click_message()
            expected_click_message = 'You have done a dynamic click'
            assert click_message == expected_click_message, \
                f'Expected dynamic click message to be' \
                f' \'{expected_click_message}\' but got {click_message}'

        @allure.title('Test user can double-click on a button.')
        def test_double_click_on_the_button_double_click_me(self, driver):
            """Test user can double-click on a button."""
            buttons_page = ButtonsPage(driver, self.buttons_page_link)
            buttons_page.open()
            buttons_page.perform_double_click()
            click_message = buttons_page.get_double_click_message()
            expected_click_message = 'You have done a double click'
            assert click_message == expected_click_message, \
                f'Expected double click message to be' \
                f' \'{expected_click_message}\' but got {click_message}'

        @allure.title('Test user can right-click on a button.')
        def test_right_click_on_the_button_right_click_me(self, driver):
            """Test user can right-click on a button."""
            buttons_page = ButtonsPage(driver, self.buttons_page_link)
            buttons_page.open()
            buttons_page.perform_right_click()
            click_message = buttons_page.get_right_click_message()
            expected_click_message = 'You have done a right click'
            assert click_message == expected_click_message, \
                f'Expected right click message to be' \
                f' \'{expected_click_message}\' but got {click_message}'

    @allure.feature('Links')
    class TestLinks:
        """Class represents Links tab tests."""
        links_page_link = 'https://demoqa.com/links'
        links_page_broken_link = 'https://demoqa.com/bad-request'
        links_page_created_link = 'https://demoqa.com/created'
        links_page_no_content_link = 'https://demoqa.com/no-content'
        links_page_moved_link = 'https://demoqa.com/moved'
        links_page_unauthorized_link = 'https://demoqa.com/unauthorized'
        links_page_forbidden_link = 'https://demoqa.com/forbidden'
        links_page_not_found_link = 'https://demoqa.com/invalid-url'

        @allure.title('Test user can open a new tab on home button.')
        def test_link_home(self, driver):
            """Test user can open a new tab on home button."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, \
                f'Broken link or link incorrect after' \
                f' click on home simple link {self.links_page_link}' \
                f'\nError: {current_url}'

        @allure.title('Test user can send a Bad Request API call.')
        def test_broken_link(self, driver):
            """Test user can send a Bad Request API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = links_page.check_broken_link(self.links_page_broken_link)
            expected_status_code = 400
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_broken_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can open a new tab on dynamic home button.')
        def test_dynamic_link_home(self, driver):
            """Test user can open a new tab on dynamic home button."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url, \
                f'Broken link or link incorrect after' \
                f' click on home simple link {self.links_page_link}' \
                f'\nError: {current_url}'

        @allure.title('Test user can send a Created API call.')
        def test_created_link(self, driver):
            """Test user can send a Created API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = \
                links_page.check_created_link(self.links_page_created_link)
            expected_status_code = 201
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_created_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can send a No Content API call.')
        def test_no_content_link(self, driver):
            """Test user can send a No Content API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = \
                links_page.check_no_content_link(self.links_page_no_content_link)
            expected_status_code = 204
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_no_content_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can send a Moved API call.')
        def test_moved_link(self, driver):
            """Test user can send a Moved API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = links_page.check_moved_link(self.links_page_moved_link)
            expected_status_code = 301
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_moved_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can send an Unauthorized API call.')
        def test_unauthorized_link(self, driver):
            """Test user can send an Unauthorized API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = \
                links_page.check_unauthorized_link(self.links_page_unauthorized_link)
            expected_status_code = 401
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_unauthorized_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can send a Forbidden API call.')
        def test_forbidden_link(self, driver):
            """Test user can send a Forbidden API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = \
                links_page.check_forbidden_link(self.links_page_forbidden_link)
            expected_status_code = 403
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_forbidden_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

        @allure.title('Test user can send a Not Found API call.')
        def test_not_found_link(self, driver):
            """Test user can send a Not Found API call."""
            links_page = LinksPage(driver, self.links_page_link)
            links_page.open()
            response_code, error_message = \
                links_page.check_not_found_link(self.links_page_not_found_link)
            expected_status_code = 404
            assert response_code == expected_status_code, \
                f'Status code from {self.links_page_not_found_link}' \
                f' should be {expected_status_code} but got {response_code}' \
                f'\nError: {error_message}'

    @allure.feature('Broken Links')
    class TestBrokenLinks:
        """Class represents Broken Links - Images tab tests."""
        broken_links_page_link = 'https://demoqa.com/broken'

        @allure.title('Test user can see a valid image.')
        def test_valid_image_on_page(self, driver):
            """Test user can see a valid image."""
            broken_links_page = BrokenLinksPage(driver, self.broken_links_page_link)
            broken_links_page.open()
            response_code, content_type, error_message = \
                broken_links_page.check_valid_image_for_200_response_and_content_type()
            assert response_code == 200, \
                f'Status code from valid image should be 200 but got {response_code}' \
                f'\nError: {error_message}'
            assert content_type == 'image/jpeg', \
                f'Invalid content {content_type}, image/jpeg expected'

        @allure.title('Test broken image has wrong content.')
        def test_broken_image_on_page(self, driver):
            """Test broken image has wrong content."""
            broken_links_page = BrokenLinksPage(driver, self.broken_links_page_link)
            broken_links_page.open()
            response_code, content_type, error_message = \
                broken_links_page.check_broken_image_for_200_response_and_content_type()
            assert content_type != 'image/jpeg', \
                f'Invalid content {content_type}, expected no to be image/jpeg.' \
                f' Error: {error_message}'
            assert response_code == 200, f'Expected 200 code, got {response_code}.' \
                                         f' Error: {error_message}'

        @allure.title('Test user goes to a correct source from a link.')
        def test_valid_link(self, driver):
            """Test user goes to a correct source from a link."""
            broken_links_page = BrokenLinksPage(driver, self.broken_links_page_link)
            broken_links_page.open()
            href_link, current_url = broken_links_page.check_valid_link()
            assert href_link == current_url, \
                f'Broken link or link incorrect after ' \
                f'click on home simple link: {self.broken_links_page_link}' \
                f'\nError: {current_url}'

        @allure.title('Test user goes to a page with 500 code from a broken link.')
        def test_broken_link(self, driver):
            """Test user goes to a page with 500 code from a broken link."""
            broken_links_page = BrokenLinksPage(driver, self.broken_links_page_link)
            broken_links_page.open()
            response_code, current_url, error_message = broken_links_page.check_broken_link()
            assert response_code == 500, \
                f'Status code from {current_url} should be 500 but got {response_code}' \
                f'\nError: {error_message}'

    @allure.feature('Upload And Download')
    class TestUploadAndDownload:
        """Class represents Upload and Download tab tests."""
        upload_and_download_page_link = 'https://demoqa.com/upload-download'

        @allure.title('Test user can upload file.')
        def test_upload_file(self, driver):
            """Test user can upload file."""
            upload_and_download_page = \
                UploadAndDownloadPage(driver, self.upload_and_download_page_link)
            upload_and_download_page.open()
            file_name, uploaded_file_name = upload_and_download_page.upload_file()
            assert file_name == uploaded_file_name, \
                f'Expected {file_name} to be equal to {upload_and_download_page} after upload'

        @allure.title('Test user can download file.')
        def test_download_file(self, driver):
            """Test user can download file."""
            upload_and_download_page = \
                UploadAndDownloadPage(driver, self.upload_and_download_page_link)
            upload_and_download_page.open()
            is_file_downloaded = upload_and_download_page.is_file_downloaded()
            assert is_file_downloaded is True, \
                f'Expected file to be downloaded (download is True) ' \
                f'but got {is_file_downloaded} instead'

    @allure.feature('Dynamic Properties')
    class TestDynamicProperties:
        """Class represents DynamicProperties tab tests."""
        dynamic_properties_page_link = 'https://demoqa.com/dynamic-properties'

        @allure.title('Test user can click on a button after 5 seconds.')
        def test_clickable_button(self, driver):
            """Test user can click on a button after 5 seconds."""
            dynamic_properties_page = \
                DynamicPropertiesPage(driver, self.dynamic_properties_page_link)
            dynamic_properties_page.open()
            is_clickable = dynamic_properties_page.is_button_enabled()
            assert is_clickable is True, \
                'Button should be clickable, but it isn\'t on dynamic_properties_page'

        @allure.title('Test button change color after 5 seconds.')
        def test_change_of_color(self, driver):
            """Test button change color after 5 seconds."""
            dynamic_properties_page = \
                DynamicPropertiesPage(driver, self.dynamic_properties_page_link)
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_change_of_color()
            assert color_before != color_after, \
                f'Color {color_before} should change, but it isn\'t. Got {color_after} after'

        @allure.title('Test button appear after 5 seconds.')
        def test_button_appearance(self, driver):
            """Test button appear after 5 seconds."""
            dynamic_properties_page = \
                DynamicPropertiesPage(driver, self.dynamic_properties_page_link)
            dynamic_properties_page.open()
            is_appeared = dynamic_properties_page.is_button_appeared()
            assert is_appeared is True, \
                'Button should appear, but it isn\'t on dynamic_properties_page'
