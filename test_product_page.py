from .pages.product_page import ProductPage
import pytest

# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])
# def test_guest_can_add_product_to_basket(browser, link):
#     PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(link))

#     product_page = ProductPage(browser, PRODUCT_URL)
#     product_page.open()
#     product_page.add_product_to_basket()


@pytest.mark.parametrize('link', [207])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    PRODUCT_URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_{link}'
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('link', [207])
def test_guest_cant_see_success_message(browser, link):
    PRODUCT_URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_{link}'
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('link', [207])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    PRODUCT_URL = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_{link}'
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.is_element_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # гость может перейти на страницу логина со страницы Х"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()