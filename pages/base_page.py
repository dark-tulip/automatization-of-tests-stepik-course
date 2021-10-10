from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from stepik.conftest import browser
from .locators import BasePageLocators


class BasePage():
    # Constructor of base class
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    # Open page by objects url
    def open(self):
        self.browser.get(self.url)


    # абстрактный метод, проверяющий, что элемент появляется на странице в течение заданного времени
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True


    # абстрактный метод, который проверяет, что элемент НЕ появляется на странице в течение заданного времени
    def is_element_not_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()


    # Найдена ссылка для регистрации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link not found on page'


    def should_not_be_products_on_basket(self):
        assert self.is_element_not_present(*BasePageLocators.BASKET_ITEMS_CONTAINER), 'Find products in empty basket but should not be'


    def should_be_msg_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MSG), 'Message about empty basket is NOT presented'


    def go_to_basket_from_header(self):
        link = self.browser.find_element(*BasePageLocators.PRODUCTS_BASKET)
        link.click()



