from gettext import gettext

# Page Object для страницы товара

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # метод добавления товара в корзину
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_cart_button.click()

    # проверка сообщения о том, что товар добавлен в корзину
    def should_be_message_with_productName(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED_NAME), "The name of added product is not presented"

    # проверка сообщения со стоимостью корзины
    def should_be_message_with_productCost(self):
        assert self.is_element_present(*ProductPageLocators.COST_ADDED_NAME), "The cost of added product is not presented"

    # Название товара в сообщении должно совпадать с товаром, который добавили
    def should_be_correct_book_name(self):
        bookname = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        bookaddedname = self.browser.find_element(*ProductPageLocators.BOOK_ADDED_NAME).text
        assert bookname == bookaddedname, "The name of added product is not match"

    # стоимость корзины должна совпадать с ценой добавленного товара
    def should_be_correct_cart_cost(self):
        bookcost = self.browser.find_element(*ProductPageLocators.BOOK_COST).text
        costaddedname = self.browser.find_element(*ProductPageLocators.COST_ADDED_NAME).text
        assert bookcost == costaddedname, "The cost of added product is not match"


