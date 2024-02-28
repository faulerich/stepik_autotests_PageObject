
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_COST = (By.CSS_SELECTOR, "p.price_color")
    BOOK_ADDED_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_ADDED_NAME = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
