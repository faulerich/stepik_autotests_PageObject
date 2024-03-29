
# 4.2.2
# базовая страница, от которой будут унаследованы все остальные классы.
# в ней мы опишем вспомогательные методы для работы с драйвером.

import math
from .locators import BasePageLocators, MainPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    # конструктор (метод, который вызывается, когда мы создаем объект) с неявным ожиданием в 10 сек
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    # метод "open" должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод "is_element_present" будет перехватывать исключения (how - как искать, what - что искать (селектор))
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # если мы хотим проверить, что какой-то элемент исчезает,
    # то следует воспользоваться явным ожиданием вместе с функцией until_not,
    # в зависимости от того, какой результат мы ожидаем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # подсчет значения выражения и ввод ответа
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # метод проверки наличия ссылки, которая ведет на форму логина
    def should_be_login_link(self):
        # * указывает на то, что передаем пару (тип локатора и его значение) и ее надо распаковать
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # метод нажатия ссылки логина (переход на страницу логина)
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # проверка того, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

        # метод перехода в корзину
    def go_to_cart_page(self):
        btn = self.browser.find_element(*MainPageLocators.BASKET_BTN)
        btn.click()

