import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FillingForm():

    def __init__(self, browser):
        self.driver = browser
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#continue")))

    @allure.step("Заполнение полей для доставки")
    def form(self, first_name, last_name, index):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
