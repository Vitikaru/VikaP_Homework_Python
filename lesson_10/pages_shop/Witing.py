import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Witing():

    def __init__(self, browser):
        self.driver = browser

    @allure.step("Проверка суммы заказа")
    def waiting_text(self):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.summary_total_label"), "$58.29"))
        assert "$58.29" in self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
