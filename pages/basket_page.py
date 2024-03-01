
# PageObject для страницы корзины

from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):

    # проверка, что в корзине нет товаров
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_CARD), \
            "Product is presented, but should not be"

    # проверка наличия сообщения об отсутствии товаров в корзине
    def should_be_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), \
            "No empty basket message, but it should be"
