from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"
    # Создаем экземпляр страницы - передаем экземпляр драйвера и адрес страницы
    page = MainPage(browser, link)

    # Открываем страницу и переходим по ссылке
    page.open()
    page.go_to_login_page()

    page.should_be_login_link()
