from stepik.conftest import browser
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_forms_on_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.browser.current_url, 'login url is not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'LOGIN_FORM not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'REGISTER_FORM not found on page'

    def register_new_user(self, email, password):
        # Добавьте в LoginPage метод register_new_user(email, password), который принимает две строки и регистрирует пользователя. 
        # Реализуйте его, описав соответствующие элементы страницы.
        self.browser.find_element(*LoginPageLocators.registration_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.registration_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.registration_password_repeat).send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.registration_button)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()


