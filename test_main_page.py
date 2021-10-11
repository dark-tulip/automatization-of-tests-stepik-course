# Запустите тесты командой:
# pytest -v --tb=line --language=en test_main_page.py
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Создаем экземпляр страницы - передаем экземпляр драйвера и адрес страницы
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)

        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_forms_on_login_page()


    def test_guest_should_see_login_link(self, browser):  
        link = "http://selenium1py.pythonanywhere.com/"   
        page = MainPage(browser, link)

        page.open()
        page.should_be_login_link()


@pytest.mark.basket_guest
class TestBasketFromMainPage():
    @pytest.mark.new
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Гость открывает главную страницу 
        # Переходит в корзину по кнопке в шапке сайта
        # Ожидаем, что в корзине нет товаров
        # Ожидаем, что есть текст о том что корзина пуста 
        link = "http://selenium1py.pythonanywhere.com/"

        main_page = MainPage(browser, link)
        main_page.open()
        
        main_page.go_to_basket_from_header()
        main_page.should_not_be_products_on_basket()
        main_page.should_be_msg_about_empty_basket()

