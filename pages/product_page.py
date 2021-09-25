from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math


class ProductPage(BasePage):

    def can_add_to_busket(self):
        add_to_busket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_busket_button.click()

        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        # Для решения задачки внутри алерта
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
