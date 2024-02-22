
# 4.2.2
# базовая страница, от которой будут унаследованы все остальные классы.
# в ней мы опишем вспомогательные методы для работы с драйвером.

from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # конструктор (метод, который вызывается, когда мы создаем объект) с неявным ожиданием в 10 сек
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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