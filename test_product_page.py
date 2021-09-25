from stepik.pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    '''
        Тест кейс для проверки того, что юзер может добавить продукт в корзину
    '''
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.can_add_to_busket()
