"""Module contains tests for Widgets tab on the site.

Contains tabs:
Accordian,
"""
import pytest
from ..pages import AccordianPage


class TestWidgetsPage:
    """Class represents Widgets tab.
    Accordian,
    """

    class TestAccordianPage:
        """Class represents Accordian tab."""
        accordian_link = 'https://demoqa.com/accordian'

        @pytest.mark.parametrize('order', ['first', 'second', 'third'])
        def test_accordian(self, driver, order: str) -> None:
            """Test user can fill the form and sent it."""
            accordian_page = AccordianPage(driver, self.accordian_link)
            accordian_page.open()
            title, content = accordian_page.check_accordian(order)
            self.check_title(order, title)
            self.check_content(order, content)

        def check_title(self, accordian_order: str, accordian_title: str) -> None:
            """Check title of accordian."""
            match accordian_order:
                case 'first':
                    assert accordian_title == 'What is Lorem Ipsum?', \
                        f'Expected first accordian title to be \'What is Lorem Ipsum?\'' \
                        f'Got: {accordian_title}'
                case 'second':
                    assert accordian_title == 'Where does it come from?', \
                        f'Expected first accordian title to be \'Where does it come from?\'' \
                        f'Got: {accordian_title}'
                case 'third':
                    assert accordian_title == 'Why do we use it?', \
                        f'Expected first accordian title to be \'Why do we use it?\'' \
                        f'Got: {accordian_title}'

        def check_content(self, accordian_order: str, accordian_content: str) -> None:
            """Check content of accordian."""
            assert accordian_content is not None, \
                'Expecter to have content of accordian.' \
                f'Got nothing. Accordian number: {accordian_order}'
