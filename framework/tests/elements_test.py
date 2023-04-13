from random import randint, choice
from ..pages import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements():
    class TestTextBox():
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, \
                output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, \
                f'Entered full name was {full_name} which doesn\'t match output full name {output_name}'
            assert email == output_email, \
                f'Entered email was {email} which doesn\'t match output email {output_email}'
            assert current_address == output_current_address, \
                f'Entered current address was {current_address} ' \
                f'which doesn\'t match output current address {output_current_address}'
            assert permanent_address == output_permanent_address, \
                f'Entered permanent address was {permanent_address} ' \
                f'which doesn\'t match output permanent address {output_permanent_address}'

    class TestCheckBox():
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_fill_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, \
                f'Checked checkboxes {input_checkboxes} ' \
                f'are not matching output result checkboxes {output_result}'

    class TestRadioButton():
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            actions = ['yes', 'impressive', 'no']
            for action in actions:
                radio_button_page.click_on_the_radio_button(action)
                output = radio_button_page.get_output_result()
                assert action.title() == output, f'Action {action} don\'t match the rusult {output}'

    class TestWebTable():
        web_page_link = 'https://demoqa.com/webtables'

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            new_person = web_table_page.add_new_person(1)
            table = web_table_page.check_added_person()
            assert new_person in table, \
                f'New person {new_person} should be in the table {table} but it isn\'t'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            key_word = web_table_page.add_new_person()[randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, \
                f'Person was not found by key word {key_word} in table {table_result}'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            fields_to_edit = ['first_name', 'last_name', 'age', 'salary', 'department', 'email']
            field_to_edit = choice(fields_to_edit)
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            edited_field = web_table_page.update_person_info(field_to_edit)
            row = web_table_page.check_search_person()
            assert edited_field in row, \
                f'Edited person info {edited_field} in {fields_to_edit} not present in edited data {row}'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            assert text == 'No rows found', \
                f'Text of search result of deleted person must be \'No rows found\' but {text} present'

        def test_table_change_number_of_rows(self, driver):
            web_table_page = WebTablePage(driver, self.web_page_link)
            web_table_page.open()
            count_of_rows = web_table_page.select_numer_of_rows()
            assert count_of_rows == [5, 10, 20, 25, 50, 100], \
                f'Available rows count is [5, 10, 20, 25, 50, 100] expected but got {count_of_rows}'
