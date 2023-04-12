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
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            import time
            web_table_page.add_new_person(3)
            time.sleep(3)
