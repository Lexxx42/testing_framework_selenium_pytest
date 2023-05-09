"""Module contains tests for Interactions tab on the site.

Contains tabs:
Sortable
"""
from ..pages import SortablePage


class TestInteractionsPage:
    """Class represents Widgets tab.
    Sortable
    """

    class TestSortablePage:
        """Class represents Sortable tab tests."""
        sortable_page_link = 'https://demoqa.com/accordian'

        def test_accordian(self, driver) -> None:
            """Test !."""
            sortable_page = SortablePage(driver, self.sortable_page_link)
            sortable_page.open()
