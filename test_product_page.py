import time

from selenium.webdriver.common.by import By

# Тесты, связанные со страницей товара
# Задание: добавление в корзину со страницы товара (4.3.2)

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# тест проверяет, что пользователь может добавить товар в корзину
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # выполняем метод страницы — нажимаем кнопку добавления товара
    page.solve_quiz_and_get_code()    # вычисляем значение выражения и отправляем его
    # запускаем тестовые сценарии из product_page.py
    page.should_be_message_with_productName()
    page.should_be_message_with_productCost()
    page.should_be_correct_book_name()
    page.should_be_correct_cart_cost()
