"""Module for relative imports in framework from locators."""
from .elements_page_locators import TextBoxPageLocators, \
    CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, BrokenLinksPageLocators, \
    UploadAndDownloadPageLocators, DynamicPropertiesPageLocators
from .form_page_locators import PracticeFormLocators
from .alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
from .widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators, \
    TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from .interactions_page_locators import SortablePageLocators, SelectablePageLocators, \
    ResizablePageLocators, DroppablePageLocators
