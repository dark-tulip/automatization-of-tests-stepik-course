from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    '''
        Тест кейс для проверки того, что юзер может добавить продукт в корзину
    '''
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
