
# Page Object для главной страницы сайта (4.2.3)

# импорт базового класса BasePage
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

# класс MainPage - наследник класса BasePage
# он будет иметь доступ ко всем атрибутам и методам BasePage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


