import pytest

# Тесты, связанные со страницей товара
# Задание: добавление в корзину со страницы товара (4.3.2)

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time

# тест проверяет, что на странице товара есть ссылка на страницу логина
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# тест проверяет, что можно перейти на страницу логина со страницы товара
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    # login_page = ProductPage(browser, browser.current_url)
    # login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage():
    # тест проверяет, что пользователь может добавить товар в корзину
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_cart()  # выполняем метод страницы — нажимаем кнопку добавления товара
        # solve_quiz_and_get_code() закомментировал, т.к. сейчас используем другую ссылку, без акции
        #page.solve_quiz_and_get_code()  # вычисляем значение выражения и отправляем его
        # запускаем тестовые сценарии из product_page.py
        page.should_be_message_with_productName()
        page.should_be_message_with_productCost()
        page.should_be_correct_book_name()
        page.should_be_correct_cart_cost()

    # проверяем, что при открытии страницы нет сообщения об успешном добавлении в корзину
    # тест должен проходить успешно, т.к. сообщения действительно нет
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # фикстура открывает страницу регистрации, регистрирует нового пользователя и проверяет, что он залогинен
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = email + "_123"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()