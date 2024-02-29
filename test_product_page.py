
import pytest

# Тесты, связанные со страницей товара
# Задание: добавление в корзину со страницы товара (4.3.2)

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

# тест проверяет, что пользователь может добавить товар в корзину
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # выполняем метод страницы — нажимаем кнопку добавления товара
    page.solve_quiz_and_get_code()    # вычисляем значение выражения и отправляем его
    # запускаем тестовые сценарии из product_page.py
    page.should_be_message_with_productName()
    page.should_be_message_with_productCost()
    page.should_be_correct_book_name()
    page.should_be_correct_cart_cost()

# тест проверяет, что на странице товара есть ссылка на страницу логина
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# тест проверяет, что можно перейти на страницу логина со страницы товара
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    #login_page = ProductPage(browser, browser.current_url)
    #login_page.should_be_login_page()


