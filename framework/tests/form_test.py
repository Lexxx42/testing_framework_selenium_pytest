from ..pages import PracticeFormPage


class TestForm:
    class TestPracticeForm:
        practice_form_link = 'https://demoqa.com/automation-practice-form'

        def test_form(self, driver):
            form_page = PracticeFormPage(driver, self.practice_form_link)
            form_page.open()
            input_data_person, date_of_birth, subject = form_page.fill_form_fields()
            output_data = form_page.form_result()
            assert input_data_person.first_name + ' ' + input_data_person.last_name == output_data[0], \
                f'Input data in form: {input_data_person.first_name}' \
                f' {input_data_person.last_name} should match output result. Got {output_data[0]}'
            assert input_data_person.email == output_data[1], \
                f'Email input in form: {input_data_person.email} ' \
                f'should match output result. Got {output_data[1]}'
            assert input_data_person.mobile[:10] == output_data[3], \
                f'Mobile input in form: {input_data_person.mobile} ' \
                f'should match output result. Got {output_data[3]}'
            assert subject == output_data[5], \
                f'Subject input in form: {subject} ' \
                f'should match output result. Got {output_data[5]}'
            assert input_data_person.current_address == output_data[8], \
                f'Current address in form: {input_data_person.current_address} ' \
                f'should match output result. Got {output_data[8]}'
