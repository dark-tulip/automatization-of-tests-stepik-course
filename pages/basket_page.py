from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket_from_header(self):
        link = self.browser.find_element(*BasePageLocators.PRODUCTS_BASKET)
        link.open()

    def should_not_be_products_on_basket(self):
        assert self.is_element_not_present(*BasePageLocators.BASKET_ITEMS_CONTAINER), 'Find products in empty basket but should not be'


    def should_be_msg_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MSG), 'Message about empty basket is NOT presented'

