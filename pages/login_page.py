
# Page Object для страницы логина (4.2.8)

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # в данном случае проверяем что подстрока "login" есть в текущем url браузера
        assert "login" in self.browser.current_url, "Incorrect login url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрирует нового пользователя
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        input_email.send_keys(email)
        input_psw = self.browser.find_element(*LoginPageLocators.REGISTER_PSW_FIELD)
        input_psw.send_keys(password)
        input_psw_conf = self.browser.find_element(*LoginPageLocators.REGISTER_PSW_CONFIRM_FIELD)
        input_psw_conf.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        reg_btn.click()