
# Page Object для главной страницы сайта (4.2.3)

# импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By

# класс MainPage - наследник класса BasePage
# он будет иметь доступ ко всем атрибутам и методам BasePage
class MainPage(BasePage):

    # функция нажатия ссылки логина (переход на страницу логина)
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()