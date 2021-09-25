# Запустите тесты командой:

# pytest -v --tb=line --language=en test_main_page.py


from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    '''
        Тест кейс для проверки того что новый юзер может зарегистрироваться
    '''
    link = "http://selenium1py.pythonanywhere.com/"

    # Создаем экземпляр страницы - передаем экземпляр драйвера и адрес страницы
    page = MainPage(browser, link)

    # Открываем страницу логина и регистрации
    page.open()

    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
