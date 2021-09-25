from .base_page import BasePage
from .locators import MainPageLocators  # импортируем класс с локаторами
from .login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        # Звездочка для автораспаковки кортежа
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        # Найдена ссылка для регистрации
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "**** Login link NOT FOUND ****"
