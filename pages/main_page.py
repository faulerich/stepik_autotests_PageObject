
# Page Object для главной страницы сайта (4.2.3)

# импорт базового класса BasePage
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

# класс MainPage - наследник класса BasePage
# он будет иметь доступ ко всем атрибутам и методам BasePage
class MainPage(BasePage):

    # метод проверки наличия ссылки, которая ведет на форму логина
    def should_be_login_link(self):
        # * указывает на то, что передаем пару (тип локатора и его значение) и ее надо распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # метод нажатия ссылки логина (переход на страницу логина)
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
