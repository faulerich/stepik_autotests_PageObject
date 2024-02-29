
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PSW_FIELD = (By.NAME, "registration-password1")
    REGISTER_PSW_CONFIRM_FIELD = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_COST = (By.CSS_SELECTOR, "p.price_color")
    BOOK_ADDED_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_ADDED_NAME = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
