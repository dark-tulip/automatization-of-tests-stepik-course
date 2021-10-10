from selenium.webdriver.common.by import By
# выносим селекторы во внешнюю переменную


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # 1. В файле locators.py создайте класс LoginPageLocators
    # 2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    
    PRODUCTS_BASKET = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner')
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, '.basket-items')
