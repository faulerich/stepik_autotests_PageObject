
import pytest

# Тесты, связанные со страницей товара (появление/исчезновение сообщений)
# Задание: отрицательные проверки (4.3.6)

from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# проверяем, что при добавлении в корзину нет сообщения об успешном добавлении
# тест должен падать, т.к. это не так

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

# проверяем, что при открытии страницы нет сообщения об успешном добавлении в корзину
# тест должен проходить успешно, т.к. сообщения действительно нет

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# проверяем, что сообщение об успешном добавлении товара в корзину исчезает после добавления товара
# тест должен падать, т.к. оно не исчезает

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear()
