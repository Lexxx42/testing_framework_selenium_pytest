"""Module contains tests for Forms tab on the site.

Contains tabs:
Practice Form.
"""
from ..pages import PracticeFormPage


class TestForm:
    """Class represents Practice Form tab.
    Contains tabs:
    Practice Form.
    """

    class TestPracticeForm:
        """Class represents Practice Form tab."""
        practice_form_link = 'https://demoqa.com/automation-practice-form'

        def test_form(self, driver):
            """Test user can fill the form and sent it."""
            form_page = PracticeFormPage(driver, self.practice_form_link)
            form_page.open()
            input_data, date_of_birth, subject = form_page.fill_form_fields()
            output_data = form_page.check_form_results()
            assert input_data.first_name + ' ' + input_data.last_name == output_data[0], \
                f'Input data in form: {input_data.first_name}' \
                f' {input_data.last_name} should match output result. Got {output_data[0]}'
            assert input_data.email == output_data[1], \
                f'Email input in form: {input_data.email} ' \
                f'should match output result. Got {output_data[1]}'
            assert input_data.mobile[:10] == output_data[3], \
                f'Mobile input in form: {input_data.mobile} ' \
                f'should match output result. Got {output_data[3]}'
            assert subject == output_data[5], \
                f'Subject input in form: {subject} ' \
                f'should match output result. Got {output_data[5]}'
            assert input_data.current_address == output_data[8], \
                f'Current address in form: {input_data.current_address} ' \
                f'should match output result. Got {output_data[8]}'
