
# 4.2.4 Первый тест на основе Page Object

from selenium.webdriver.common.by import By
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

# тест проверяет, что пользователь видит ссылку на страницу логина
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# тест проверяет, что пользователь может перейти по ссылке на страницу логина
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина