from ..pages import PracticeFormPage


class TestForm:
    class TestPracticeForm:
        practice_form_link = 'https://demoqa.com/automation-practice-form'
        def test_form(self, driver):
            form_page = PracticeFormPage(driver, self.practice_form_link)
            form_page.open()
            form_page.fill_form_fields()
