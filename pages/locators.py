# выносим селекторы во внешнюю переменную

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():   # 1. В файле locators.py создайте класс LoginPageLocators

    # 2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators

    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
