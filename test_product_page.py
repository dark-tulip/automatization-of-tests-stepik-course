from stepik.pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.login
class TestLoginFromProductPage():
    # Чтобы функция запускалась автоматически перед каждым тест-кейсом
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):        
        self.product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        self.product_page = ProductPage(browser, self.product_link)


    def test_guest_should_see_login_link(self):
        page = self.product_page
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        # гость может перейти на страницу логина со страницы Х"
        page = self.product_page
        page.open()
        page.go_to_login_page()


@pytest.mark.add_to_basket
class TestAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):        
        self.product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        self.product_page = ProductPage(browser, self.product_link)


    def test_guest_cant_see_success_message(self, browser):
        self.product_page.open()
        self.product_page.should_not_be_success_message()


    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        self.product_page.open()
        self.product_page.add_product_to_basket()
    

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        product_page = self.product_page
        product_page.open()
        
        product_page.go_to_basket_from_header()
        product_page.should_not_be_products_on_basket()
        product_page.should_be_msg_about_empty_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'

        time_id = str(time.time()) 
        email = time_id + "@fakemail.org"
        password = time_id

        self.login_page = LoginPage(browser, LOGIN_URL)
        self.login_page.open()
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.add_product_to_basket()



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    PRODUCT_URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    PRODUCT_URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_element_disappeared()

